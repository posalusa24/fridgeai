import cv2


def get_frames(shape, count, interval):
    frames = []

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cv2.namedWindow("FridgeAI Camera")

    for i in range(count * interval):
        ret, frame = cam.read()
        preview_frame = cv2.flip(frame, 1)
        if i % interval == 0:
            frames.append(cv2.resize(frame, shape))
            # turn the preview frame white to simulate a camera flash
            preview_frame = cv2.rectangle(
                preview_frame,
                (0, 0),
                (preview_frame.shape[1], preview_frame.shape[0]),
                (255, 255, 255),
                -1
            )
        cv2.imshow("FridgeAI Camera", preview_frame)
        cv2.waitKey(1)

    cv2.destroyAllWindows()
    cam.release()

    return frames
