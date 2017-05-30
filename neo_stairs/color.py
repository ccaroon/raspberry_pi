import neopixel
import random

# NOTE: For some reason the colors passed to neopixel.Color are NOT RGB order.
def Color(r,g,b):
    return neopixel.Color(g,r,b)

def White():
    return Color(255,255,255)

def Black():
    return Color(0,0,0)

def Red():
    return Color(255,0,0)

def Green():
    return Color(0,255,0)

def Blue():
    return Color(0,0,255)

def Random():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return Color(r,g,b)
