#!/usr/bin/env python3
# this is an example to test if the bot can detect the black colour

from ev3dev2.sensor.lego import ColorSensor, INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.display import Display
from time import sleep

# Initialise the display, colour sensors and motors
display = Display()
cl_1 = ColorSensor(INPUT_1)
# cl_2 = ColorSensor(INPUT_2)
# cl_3 = ColorSensor(INPUT_3)
cl_4 = ColorSensor(INPUT_4)
motors = MoveTank(OUTPUT_B, OUTPUT_C)

# INPUT_1 is the right colour sensor, INPUT_4 is left
cl_1.mode = ColorSensor.MODE_COL_COLOR
cl_4.mode = ColorSensor.MODE_COL_COLOR

while True:
    if cl_1.color == ColorSensor.COLOR_BLACK:
        print("Black detected")
        display.text_pixels("Black Detected", x=10, y=10, clear_screen=True)
        display.update()
    elif cl_1.color == ColorSensor.COLOR_GREEN:
        print("Green detected")
        display.text_pixels("Green Detected", x=10, y=30, clear_screen=False)
        display.update()
    else:
        print("Other color detected")


def followLine():
    # the direction variable gets returned by this function which will determine which
    # way the robot goes based on the colour sensors.
    direction = ""
    if cl_1.color == ColorSensor.COLOR_BLACK:
        direction = "right"
    if cl_4.color == ColorSensor.COLOR_BLACK:
        direction = "left"
    if cl_1.color == ColorSensor.COLOR_BLACK and cl_4.color == ColorSensor.COLOR_BLACK:
        direction = "intersection"
        # intersections will have a green square to guide to the correct direction
        # the robot must move so one of its colour sensors can detect the green
        # one way this could work is moving the robot back a little until it detects green
        
    return direction
        


