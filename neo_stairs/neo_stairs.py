#!/usr/bin/env python
import random
import time
from neopixel import *

# LED strip configuration:
LED_COUNT      = 5      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

LIT_COUNT = 2
last = [0,0];
def twinkle():
    for i in range(0,LIT_COUNT):
        strip.setPixelColor(last[i], get_color(0, 0, 0));
        last[i] = random.randint(0, LED_COUNT);

        r = random.randint(25, 255);
        g = random.randint(25, 255);
        b = random.randint(25, 255);
        strip.setPixelColor(last[i], get_color(r, g, b));

    strip.show();
    delay(150);

def delay(duration):
    time.sleep(duration/1000.0)

def walk():
    r = random.randint(0, 255);
    g = random.randint(0, 255);
    b = random.randint(0, 255);
    for i in range(0, LED_COUNT):
        strip.setPixelColor(i, get_color(r, g, b));
        strip.show();
        delay(100.0);

    delay(750.0);

# NOTE: For some reason the colors passed to Color are NOT RGB order.
def get_color(r,g,b):
    return Color(g,r,b)

if __name__ == '__main__':
    random.seed()

    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    strip.begin()

    print "Control-C to Exit"
    while True:
        # walk()
        twinkle()
