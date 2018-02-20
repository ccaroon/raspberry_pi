#!/usr/bin/env python
import RPi.GPIO as GPIO
import datetime
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT, initial=0)
#GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
#    if GPIO.input(6) == GPIO.HIGH:
#        print('\nDown  at ' + str(datetime.datetime.now()))
   GPIO.output(17,1)
   time.sleep(1)
   GPIO.output(17,0)
   time.sleep(1)
 
