#!/usr/bin/env python
import argparse
import color
import strip
###############################################################################
parser = argparse.ArgumentParser();
parser.add_argument("action", choices=["random", "cylon", "rgb"])
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
elif (action == "rgb"):
    r = args.red
    g = args.green
    b = args.blue
    stairs.set_color(color.Color(r,g,b))
