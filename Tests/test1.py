#!/usr/bin/env python3
# this is an example to test if the bot can detect the black colour

from ev3dev2.sensor import Sensor, INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor
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

display.text_pixels("Hello!", x=10, y=10, clear_screen=True)
display.update()

# while True:
#     display.clear()
#     display.text_pixels("Right:" + str(cl_1.color_name) + " Left:" + str(cl_4.color_name), x=10, y=30, clear_screen=False)
#     display.update()


def followLine():
    detectable_colours = [ColorSensor.COLOR_BLACK, ColorSensor.COLOR_GREEN, ColorSensor.COLOR_RED]
    # the direction variable gets returned by this function which will determine which
    # way the robot goes based on the colour sensors.
    direction = ""
    if cl_1.color == ColorSensor.COLOR_BLACK:
        direction = "right"
    if cl_4.color == ColorSensor.COLOR_BLACK:
        direction = "left"
    if cl_1.color not in detectable_colours and cl_4.color not in detectable_colours:
        direction = "forward"
    # intersections will have a green square to guide to the correct direction
    if cl_1.color == ColorSensor.COLOR_GREEN:
        direction = "intersectionRight"
    if cl_4.color == ColorSensor.COLOR_GREEN:
        direction = "intersectionLeft"
        
    return direction

while True:
    direction = followLine()
    if direction == "right":
        motors.on(left_speed=0, right_speed=20)
    elif direction == "left":
        motors.on(left_speed=20, right_speed=0)
    elif direction == "forward":
        motors.on(left_speed=20, right_speed=20)
    elif direction == "intersectionRight":
        motors.on(left_speed=0, right_speed=20)
    elif direction == "intersectionLeft":
        motors.on(left_speed=20, right_speed=0)
    else:
        motors.off()