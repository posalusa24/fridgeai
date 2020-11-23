"""
import cv2
import time

cam = cv2.VideoCapture(0)
cv2.namedWindow("FridgeAI")

INTERVAL = 10 # smaller means more frames per second

for i in range(50):
    ret, frame = cam.read()
    cv2.imshow("FridgeAI", cv2.flip(frame, 1))
    if i % INTERVAL == 0:
        cv2.imwrite("frame{}.jpg".format(int(i / INTERVAL)), frame)
        print("{} written!".format(int(i / INTERVAL)))
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
"""
items = []

def list_items():
    print("Currently stored items:")
    for i, item in enumerate(items):
        print("{}. {}".format(i + 1, item))

def scan_item():
    while True:
        # dummy scan of a Coke bottle
        print("Scanning...")
        item = "Coke"
        print("Scan result: Coke")

        option = input("[s]ave, [r]escan or [c]ancel (default 'r'): ")
        if option == "s":
            items.append(item)
            break
        elif option == "c":
            break

print("Welcome to FridgeAI Shell!")

while True:
    command = input(">> ")
    if command == "list":
        list_items()
    elif command == "scan":
        scan_item()
    elif command == "exit":
        break
    else:
        print("Unknown command. Available: list, scan, exit")
