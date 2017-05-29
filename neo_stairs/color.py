import neopixel

# NOTE: For some reason the colors passed to neopixel.Color are NOT RGB order.
def Color(r,g,b):
    return neopixel.Color(g,r,b)

def White():
    return Color(255,255,255)

def Red():
    return Color(255,0,0)

def Green():
    return Color(0,255,0)

def Blue():
    return Color(0,0,255)
