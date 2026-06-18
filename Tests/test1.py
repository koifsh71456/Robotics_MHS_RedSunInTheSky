#!/usr/bin/env python3
# this is an example to test if the bot can detect the black colour

from ev3dev2.sensor.lego import ColorSensor, INPUT_1, INPUT_2, INPUT_3, INPUT_4
from time import sleep

cl_1 = ColorSensor(INPUT_1)
# cl_2 = ColorSensor(INPUT_2)
# cl_3 = ColorSensor(INPUT_3)
cl_4 = ColorSensor(INPUT_4)

cl_1.mode = ColorSensor.MODE_COL_COLOR

if cl_1.color == ColorSensor.COLOR_BLACK:
    print("Black detected")
elif cl_1.color == ColorSensor.COLOR_GREEN:
    print("Green detected")
else:
    print("Other color detected")
