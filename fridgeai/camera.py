import platform
import cv2
if platform.machine() == "armv6l":
    import picamera


def get_frames(shape, count, interval):
    if platform.machine() == "armv6l":
        print("This is a Pi! Using picamera...")
        return _get_frames_picamera(shape, count, interval)
    else:
        return _get_frames_webcam(shape, count, interval)


def _get_frames_picamera(shape, count, interval):
    frames = []

    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 30
    raw_capture = picamera.PiRGBArray(camera, size=(640, 480))

    for i, frame in enumerate(camera.capture_continuous(
            raw_capture,
            format="bgr",
            use_video_port=True)):
        if (i > count * interval):
            break
        frame = frame.array
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
        raw_capture.truncate(0)

    cv2.destroyAllWindows()
    return frames


def _get_frames_webcam(shape, count, interval):
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
