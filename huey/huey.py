#!/usr/bin/env python

import sys
from phue import Bridge

LIGHT = 'Computer Room Lamp'
READING = 'Reading Light'

cmd = None
if len(sys.argv) <= 1:
    sys.exit(0)
else:
    cmd = sys.argv[1]

b = Bridge('192.168.1.93')

if cmd == 'connect':
   b.connect()
elif cmd == 'reading':
    color = 15000
    if len(sys.argv) == 3:
        color = int(sys.argv[2], 10)
    b.set_light(READING, 'on', True)
    b.set_light(READING, 'bri', 255)
    b.set_light(READING, 'hue', color)
    b.set_light(READING, 'sat', 255)
elif cmd == 'computer':
    b.set_light(LIGHT, 'on', True)
    b.set_light(LIGHT, 'bri', 255)
else:
    print("Unknown commmand [%s]" % (cmd))
