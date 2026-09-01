#!/usr/bin/env python3
# THIS FILE IS A TEST FOR ON_FOR_DEGREES

from ev3dev2.sensor import Sensor, INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
from ev3sim.code_helpers import wait_for_tick
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

display.text_pixels("Hello!", x=10, y=10, clear_screen=True)
display.update()


# motors.on(left_speed=20, right_speed=20)
# sleep(1)
motors.on_for_degrees(left_speed=0, right_speed=-40, degrees=270)
# sleep(1)
# motors.on(left_speed=20, right_speed=20)
# sleep(1)
# motors.on_for_degrees(left_speed=-100, right_speed=0, degrees=90)
# sleep(1)
# motors.on(left_speed=20, right_speed=20)
# sleep(1)
# motors.on_for_degrees(left_speed=-100, right_speed=0, degrees=90)
# sleep(1)
# motors.on(left_speed=20, right_speed=20)
# sleep(1)
# motors.on_for_degrees(left_speed=0, right_speed=-100, degrees=90)
# sleep(1)
# motors.on(left_speed=20, right_speed=20)