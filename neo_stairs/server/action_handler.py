import color
import neo_strip

class ActionHandler:

    def __init__(self):
        self.__strip = neo_strip.NeoPixelStrip()

    def handle(self, path, query_string):
        success = True

        if path == "/set_color":
            r = int(query_string['red'][0])
            g = int(query_string['green'][0])
            b = int(query_string['blue'][0])
            self.set_color(r,g,b)

        return(success)

    def set_color(self, red, green, blue):
        self.__strip.set_color(color.Color(red,green,blue))
