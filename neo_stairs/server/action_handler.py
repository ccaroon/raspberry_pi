import color
import neo_strip

class ActionHandler:

    def __init__():
        # Create NeoPixelStrip
        # strip = neo_strip.NeoPixelStrip()
        pass

    def handle(path, query_string):
        success = True

        if path == "/set_color":
            r = query_string['red'][0]
            g = query_string['green'][0]
            b = query_string['blue'][0]
            self.set_color(r,g,b)

        return(success)

    def set_color(red, green, blue):
        print("ActionHandler#set_color: (%s|%s|%s)" % (r,g,b))
