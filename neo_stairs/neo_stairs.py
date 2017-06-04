#!/usr/bin/env python
import argparse
import color
import strip
###############################################################################
parser = argparse.ArgumentParser();
parser.add_argument("action", choices=["random", "cylon", "rgb", "twinkle", "walk"])
parser.add_argument("--red",   type=int, default=0)
parser.add_argument("--green", type=int, default=0)
parser.add_argument("--blue",  type=int, default=0)
args = parser.parse_args();
###############################################################################
action = args.action
stairs = strip.Strip()

if (action == "random"):
    stairs.set_color(color.Random())
elif (action == "cylon"):
    stairs.cylon()
elif (action == "twinkle"):
    r = args.red
    g = args.green
    b = args.blue
    stairs.twinkle(color.Color(r,g,b))
elif (action == "walk"):
    stairs.walk()
elif (action == "rgb"):
    r = args.red
    g = args.green
    b = args.blue
    stairs.set_color(color.Color(r,g,b))
