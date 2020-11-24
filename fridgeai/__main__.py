"""Entry point of program."""
from fridgeai import shell, gui

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2 and sys.argv[1] == "gui":
        gui.init()
    else:
        shell.init()
