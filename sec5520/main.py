#!/usr/bin/env python
import argparse
import os
import time
from gpiozero import LED

import message.email
import eyes.camera
import motion.sensor

parser = argparse.ArgumentParser()
parser.add_argument("-b","--basename", default="img", help="Basename of images.")
parser.add_argument("-d","--duration", default=15, help="Capture images for <duration> seconds.")
parser.add_argument("-s","--sms", default=None, help="SMS Email Addr")
parser.add_argument("-u","--user", default=None, help="GMail User Name")
parser.add_argument("-p","--password", default=None, help="GMail Password")
args = parser.parse_args()

print("Capturing images named '{0}' for {1} seconds.".format(args.basename, args.duration))

emailer = None
if args.sms and args.user and args.password:
    emailer = message.email.Email("smtp.gmail.com", 587, {"username": args.user,  "password": args.password})

led = LED(20)
s = motion.sensor.Sensor()
c = eyes.camera.Camera("bzI5NwYtmjoAAAAAAAAhefkgNwfwe6RUExqts24p29kudGwQDf_YYYvqdiRRYZKP", args.basename)
count = 0

def capture_images():
    global count
    count += 1
    # print("\t --> Hello, World! [{0}]".format(count))

    # send_msg_timeout = 5 * 60 # In Seconds
    # if time.time() - self.last_msg_sent_at > Sensor.send_msg_timeout:
    #     self.send_text()
    #     self.last_msg_sent_at = time.time()

    led.on()

    if emailer:
        print("\t --> Sending text message...")
        emailer.send(args.sms, "Sec5520 - #{0}".format(count), "Motion Detected! Image capture underway!")

    print("\t --> Capturing Images...")
    c.capture_for(float(args.duration))

    led.off()
    # print("\t --> Sleep...")
    # time.sleep(10)

s.on_detect(capture_images)
