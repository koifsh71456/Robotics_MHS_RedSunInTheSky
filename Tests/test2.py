#!/usr/bin/env python3

from ev3dev2.sensor import Sensor, INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
# from ev3sim.code_helpers import wait_for_tick
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.display import Display
from time import sleep

# Initialise the display, colour sensors and motors
display = Display()
cl_1 = ColorSensor(INPUT_4)
ultrasonic = UltrasonicSensor(INPUT_3)
distance = ultrasonic.distance_centimeters
# cl_3 = ColorSensor(INPUT_3)
cl_4 = ColorSensor(INPUT_1)
motors = MoveTank(OUTPUT_B, OUTPUT_C)

# INPUT_4 is the right colour sensor, INPUT_1 is left
cl_1.mode = ColorSensor.MODE_COL_COLOR
cl_4.mode = ColorSensor.MODE_COL_COLOR

# Screen initialisation for robot
display.text_pixels("Hello!", x=10, y=10, clear_screen=True)
display.update()

def followLine():
    intersection_direction = "null"
    direction = ""
    # Connect the ultrasonic sensor and motors
    us = UltrasonicSensor(INPUT_2)
    motors = MoveTank(OUTPUT_B, OUTPUT_C)
    display = Display()

    if cl_1.color == ColorSensor.COLOR_BLACK:
        direction = "right"
    if cl_4.color == ColorSensor.COLOR_BLACK:
        direction = "left"
    if cl_1.color == ColorSensor.COLOR_BLACK and cl_4.color == ColorSensor.COLOR_BLACK:
        # direction = green_intersection_direction
        direction = "forward"
    if cl_1.color != ColorSensor.COLOR_BLACK and cl_4.color != ColorSensor.COLOR_BLACK:
        direction = "forward"
    if cl_1.color == ColorSensor.COLOR_GREEN:
        direction = "intersectionRight"
    if cl_4.color == ColorSensor.COLOR_GREEN:
        direction = "intersectionLeft"
    if cl_1.color == ColorSensor.COLOR_GREEN and cl_4.color == ColorSensor.COLOR_GREEN:
        direction = "bothGreen"
        
    return direction


while True:
    direction = followLine()
    if direction == "right":
        motors.on(left_speed=-5, right_speed=5, degrees=5)
    elif direction == "left":
        motors.on(left_speed=5, right_speed=-5, degrees=5)
    elif direction == "forward":
        motors.on(left_speed=10, right_speed=10, degrees=5)
    elif direction == "intersectionRight":
        motors.on(left_speed=-5, right_speed=5, degrees=5)
    elif direction == "intersectionLeft":
        motors.on(left_speed=5, right_speed=-5, degrees=5)

    