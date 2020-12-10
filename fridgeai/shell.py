"""
FridgeAI's command-line shell interface.

To add a new command, create a function with the @command decorator.
Function name must have an underscore in front.
Function docstring optionally defines a help statement for your command, which
is displayed by the 'help' command.
"""
import cv2
import os

available_commands = {}


def init():
    """Initialize command-line shell."""
    print("Welcome to FridgeAI Shell!")
    while True:
        command = input(">> ")
        if command in available_commands:
            available_commands[command]()
        else:
            print("Unknown command. Try 'help'")


def command(func):
    """Decorator for commands."""
    available_commands[func.__name__[1:]] = func
    return func


# Add commands here
@command
def _sync():
    """Sync database in background."""
    import threading
    from fridgeai import training
    thread = threading.Thread(target=training.model_sync)
    thread.daemon = True
    thread.start()


@command
def _train():
    """Train a new item."""
    import shutil
    from fridgeai import camera, training
    frames = camera.get_frames(shape=(32, 32), count=100, interval=2)
    label = input("Enter item name: ")
    os.mkdir(label)
    for i, frame in enumerate(frames):
        cv2.imwrite(os.path.join(label, 'frame{}.jpg'.format(i)), frame)
    training.send_training_data(label)
    shutil.rmtree(label)


@command
def _snap():
    """Do a dummy scan."""
    from fridgeai import camera
    camera.get_frames(shape=(32, 32), count=5, interval=5)


@command
def _add():
    """Manually add a new item."""
    from fridgeai import inventory
    label = input("Enter item name: ")
    inventory.add(label)


@command
def _list():
    """List all stored items."""
    from fridgeai import inventory
    print("Currently stored items:")
    for i, item in enumerate(inventory.list()):
        print("{}. {}".format(i + 1, item))


@command
def _scan():
    """Scan a new item using webcam."""
    from fridgeai import inventory, camera, ai
    while True:
        print("Scanning...")
        label = ai.predict(camera.get_frames((32, 32), count=5, interval=5))
        print("Scan result: {}".format(label))

        option = input("[s]ave, [r]escan or [c]ancel (default 'r'): ")
        if option == "s":
            inventory.add(label)
            break
        elif option == "c":
            break


@command
def _exit():
    """Exit the program."""
    exit()


@command
def _help():
    """Seek help."""
    print("Available commands:")
    for command in available_commands:
        print(command, " -- ", available_commands[command].__doc__)
