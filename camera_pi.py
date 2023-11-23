import io
import time
import picamera
from base_camera import BaseCamera


class Camera(BaseCamera):
    @staticmethod
    def frames():
        with picamera.PiCamera() as camera:
            # let camera warm up
            time.sleep(2)

            ###jwc n camera.resolution(300,200)
            ###jwc n camera.resolution(320,240)

            stream = io.BytesIO()
            ###jwc y for _ in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
            for _ in camera.capture_continuous(stream, 'jpeg', use_video_port=True, resize=(320,240)):
                # return current frame
                stream.seek(0)
                yield stream.read()

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()
