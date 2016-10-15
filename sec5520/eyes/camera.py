import dropbox
import os
import time
import picamera

class Camera:

    def __init__(self, db_token, basename = "img"):
        self.basename = basename
        self.dbx = dropbox.Dropbox(db_token)
        self.camera = picamera.PiCamera()
        self.camera.resolution = (960, 540)

    def capture_for(self, duration = 60):
        # with self.camera as cam:
        self.camera.start_preview()
        start_time = time.time()
        try:
            for filename in self.camera.capture_continuous("{0}_".format(self.basename) + "{timestamp:%Y-%m-%d_%H-%M-%S}.jpg"):
                # print('Captured %s' % filename)
                f = open(filename, "rb")
                self.dbx.files_upload(f.read(), "/{0}".format(os.path.basename(f.name)))
                f.close()

                if time.time() - start_time >= duration:
                    break;
        finally:
            self.camera.stop_preview()
