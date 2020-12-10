import platform
import cv2
import time
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

    with picamera.PiCamera() as camera:
        with picamera.array.PiRGBArray(camera, size=(32, 32)) as output:
            camera.resolution = (480, 640)
            camera.start_preview()
            for i, frame in enumerate(camera.capture_continuous(
                output, resize=(32, 32), format="bgr", use_video_port=True
            )):
                # output=output.reshape(32,32,3)
                # frame = cv2.resize(
                #     frame.array, (32,32), interpolation=cv2.INTER_AREA
                # )
                frames.append(frame)
                print(frame.shape)
                if i == 8:
                    break
                output.truncate(0)
                time.sleep(0.4)
            camera.stop_preview()

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
