import time
import cv2
import numpy as np
from keras.models import load_model

items = []


def main():
    print("Welcome to FridgeAI Shell!")
    while True:
        command = input(">> ")
        if command == "list":
            list_items()
        elif command == "scan":
            scan_item()
        elif command == "delete":
            delete_item()
        elif command == "exit":
            break
        else:
            print("Unknown command. Available: list, scan, exit")


def list_items():
    print("Currently stored items:")
    for i, item in enumerate(items):
        print("{}. {}".format(i + 1, item))


def scan_item():
    while True:
        print("Scanning...")
        item = predict(get_frames_from_webcam())
        print("Scan result: {}".format(item))

        option = input("[s]ave, [r]escan or [c]ancel (default 'r'): ")
        if option == "s":
            items.append(item)
            break
        elif option == "c":
            break


def delete_item():
    while True:
        print()
        list_items()
        index = int(input("Enter the item number " \
                          "to be deleted ('0' to cancel): ")) - 1
        if index >= 0 and index < len(items):
            print("Item '{}' deleted!".format(items[index]))
            items.pop(index)
            break
        elif index == -1:
            break
        else:
            print("Item does not exist!")


def get_frames_from_webcam():
    frames = []

    cam = cv2.VideoCapture(0)
    cv2.namedWindow("FridgeAI Camera")

    INTERVAL = 10

    for i in range(50):
        ret, frame = cam.read()
        cv2.imshow("FridgeAI Camera", cv2.flip(frame, 1))
        if i % INTERVAL == 0:
            frames.append(cv2.resize(frame, (32, 32)))
        if cv2.waitKey(1) == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

    return frames

def predict(images):
    """Given a list of images, output the most likely prediction."""
    data = np.array(images).astype("float") / 255.0
    model = load_model(".")
    preds = model.predict(data, batch_size=32).argmax(axis=1)
    print(preds)
    prediction = np.argmax(np.bincount(preds))

    if prediction == 0:
        prediction = "Coke"
    elif prediction == 1:
        prediction = "Emborg"
    elif prediction == 2:
        prediction = "Pepsi"
        
    return prediction

if __name__ == "__main__":
    main()
