#!/usr/bin/env python3
import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1920, 1080)
    camera.start_preview()
    time.sleep(3)
    for filename in camera.capture_continuous('img{counter:07d}.jpg'):
        print('Captured %s' % filename)
        time.sleep(5) # wait 5 seconds
