#!/usr/bin/env python
import sys
import color
import strip

if __name__ == '__main__':
    action = sys.argv[1];
    stairs = strip.Strip()

    # stairs.walk()
    # stairs.twinkle()
    if action == "red":
        stairs.set_color(color.Red())
    elif action == "green":
        stairs.set_color(color.Green())
    elif action == "blue":
        stairs.set_color(color.Blue())
    else:
        stairs.set_color(color.Random())
