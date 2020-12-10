def get_frames(shape, count, interval):
    import platform
    if platform.machine() == "armv6l":
        print("This is a Pi! Using picamera...")
        return _get_frames_picamera(shape, count, interval)
    else:
        return _get_frames_webcam(shape, count, interval)


def _get_frames_picamera(shape, count, interval):
    import picamera
    import picamera.array
    import time

    frames = []

    with picamera.PiCamera() as camera:
        with picamera.array.PiRGBArray(camera, size=shape) as output:
            camera.resolution = (128, 128)
            camera.start_preview()
            for i, frame in enumerate(camera.capture_continuous(
                output, resize=shape, format="bgr", use_video_port=True
            )):
                frames.append(frame.array)
                if i == count:
                    break
                output.truncate(0)
                time.sleep(interval / 10)
            camera.stop_preview()

    return frames


def _get_frames_webcam(shape, count, interval):
    import cv2
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
