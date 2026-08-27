#!/usr/bin/env python3
import time
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor import INPUT_2
from ev3dev2.display import Display

# Connect the ultrasonic sensor and motors
us = UltrasonicSensor(INPUT_2)


display = Display()
while True:
    display.text_pixels("Ultrasonic Test", x=10, y=10, clear_screen=True)
    display.update()