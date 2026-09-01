#!/usr/bin/env python3
 
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
 
 
while True:
    distance = ultrasonic.distance_centimeters
    display.text_pixels("{}".format(distance), x=10, y=30, clear_screen=True)
    display.update()
    motors.on(left_speed=-8, right_speed=8)
    if distance < 30:
        break
while distance > 10:
    distance = ultrasonic.distance_centimeters
    motors.on(left_speed=-15, right_speed=-15)