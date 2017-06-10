import random
from neopixel import Adafruit_NeoPixel

import color
import util

class NeoPixelStrip:

    """Singleton of a NeoPixel Strip with the parameters as defined below"""

    __instance = None

    # Singleton handling stuff
    def __init__(self):
        if NeoPixelStrip.__instance == None:
            NeoPixelStrip.__instance = NeoPixelStrip.__Instance()

    def __getattr__(self, name):
        return getattr(NeoPixelStrip.__instance, name)

    # Define instance methods here
    class __Instance:

        # LED strip configuration:
        LED_COUNT      = 150     # Number of LED pixels.
        LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
        LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
        LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
        LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
        LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

        def __init__(self):
            random.seed()

            self.__strip = Adafruit_NeoPixel(self.LED_COUNT, self.LED_PIN, self.LED_FREQ_HZ, self.LED_DMA, self.LED_INVERT, self.LED_BRIGHTNESS)
            self.__strip.begin()

        LIT_COUNT = 10
        last = [0] * LIT_COUNT
        def twinkle(self):
            while True:
                for i in range(0,self.LIT_COUNT):
                    self.__strip.setPixelColor(self.last[i], color.Black())
                    self.last[i] = random.randint(0, self.__strip.numPixels())

                    self.__strip.setPixelColor(self.last[i], color.Random())

                self.__strip.show()
                util.delay(150)

        def walk(self):
            while True:
                for i in range(0, self.__strip.numPixels()):
                    self.__strip.setPixelColor(i, color.Random())
                    self.__strip.show()
                    util.delay(100.0)

                util.delay(750.0)

        def set_color(self, color):
            for i in range(0, self.__strip.numPixels()):
                self.__strip.setPixelColor(i, color)

            self.__strip.show();

        def cylon(self):
            red = 0
            for i in range(0,self.__strip.numPixels()):
                self.__strip.setPixelColor(i, color.Color(red, 0, 0))
                red+=1

            self.__strip.show();
