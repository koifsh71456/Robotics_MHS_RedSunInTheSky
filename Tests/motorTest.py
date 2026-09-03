#!/usr/bin/env python3

from ev3dev2.sensor import Sensor, INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
from ev3sim.code_helpers import wait_for_tick
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C, MediumMotor
from ev3dev2.display import Display


display = Display()
cl_1 = ColorSensor(INPUT_4)
cl_4 = ColorSensor(INPUT_1)
m_motor = MediumMotor(OUTPUT_A)

# INPUT_4 is the right colour sensor, INPUT_1 is left
cl_1.mode = ColorSensor.MODE_COL_COLOR
cl_4.mode = ColorSensor.MODE_COL_COLOR



def getDirection():
    direction = ""
    if cl_1.color == ColorSensor.COLOR_BLACK:
        direction = "right"
    elif cl_4.color == ColorSensor.COLOR_BLACK:
        direction = "left"
    else:
        direction = "null"
    return direction

while True:
    direction = getDirection()
    if direction == "right":
        m_motor.on(30)
    elif direction == "left":
        m_motor.on(-30)
    else:
        m_motor.off()