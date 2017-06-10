import color
import neo_strip

class ActionHandler:

    def __init__(self):
        # Create NeoPixelStrip
        # strip = neo_strip.NeoPixelStrip()
        print("ActionHandler init")

    def handle(self, path, query_string):
        success = True

        if path == "/set_color":
            r = query_string['red'][0]
            g = query_string['green'][0]
            b = query_string['blue'][0]
            self.set_color(r,g,b)

        return(success)

    def set_color(self, red, green, blue):
        print("ActionHandler#set_color: (%s|%s|%s)" % (red,green,blue))
