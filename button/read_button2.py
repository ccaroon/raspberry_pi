#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT, initial=0)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        if GPIO.input(6) == GPIO.HIGH:
            GPIO.output(17,1)
        else:
            GPIO.output(17,0)
except KeyboardInterrupt:
    print "Cleaning up and exiting."
    GPIO.cleanup()
