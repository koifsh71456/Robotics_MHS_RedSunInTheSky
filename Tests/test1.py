#!/usr/bin/env python3
# this is an example to test if the bot can detect the black colour

from ev3dev2.sensor.lego import ColorSensor, INPUT_1
from time import sleep

cl = ColorSensor(INPUT_1)

cl.mode = ColorSensor.MODE_COL_COLOR

if cl.color == ColorSensor.COLOR_BLACK:
    print("Black detected")
elif cl.color == ColorSensor.COLOR_GREEN:
    print("Green detected")
else:
    print("Other color detected")
