#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_A, MediumMotor

output = MediumMotor(OUTPUT_A)

output.on_for_seconds(67,10)