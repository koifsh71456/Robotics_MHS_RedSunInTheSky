#!/usr/bin/env python3

from ev3dev2.sensor import Sensor, INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
from ev3sim.code_helpers import wait_for_tick
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C, MediumMotor
from ev3dev2.display import Display


display = Display()
ultrasonic = UltrasonicSensor(INPUT_3)
distance = ultrasonic.distance_centimeters
cl_1 = ColorSensor(INPUT_4)
cl_4 = ColorSensor(INPUT_1)
motors = MoveTank(OUTPUT_B, OUTPUT_C)

# INPUT_4 is the right colour sensor, INPUT_1 is left
cl_1.mode = ColorSensor.MODE_COL_COLOR
cl_4.mode = ColorSensor.MODE_COL_COLOR

def followLine():
    detectable_colours = [ColorSensor.COLOR_BLACK, ColorSensor.COLOR_GREEN, ColorSensor.COLOR_RED]
#     # the direction variable gets returned by this function which will determine which
#     # way the robot goes based on the colour sensors.
    direction = ""
    if cl_1.color == ColorSensor.COLOR_BLACK:
        direction = "right"
    if cl_4.color == ColorSensor.COLOR_BLACK:
        direction = "left"
    if cl_1.color == ColorSensor.COLOR_BLACK and cl_4.color == ColorSensor.COLOR_BLACK:
        direction = "forward"
    # if cl_1.color not in detectable_colours and cl_4.color not in detectable_colours:
    #     direction = "forward"
    if cl_1.color != ColorSensor.COLOR_BLACK and cl_4.color != ColorSensor.COLOR_BLACK:
        direction = "forward"
    # intersections will have a green square to guide to the correct direction
    if cl_1.color == ColorSensor.COLOR_GREEN:
        direction = "intersectionRight"
    if cl_4.color == ColorSensor.COLOR_GREEN:
        direction = "intersectionLeft"
    if cl_1.color == ColorSensor.COLOR_GREEN and cl_4.color == ColorSensor.COLOR_GREEN:
        direction = "bothGreen"
    return direction

while True:
    direction = followLine() # set followLine() to a variable so it can be used in the if statements below
    if distance > 5:
        if direction == "right":
            # When the right colour sensor detects black, the robot will turn right to follow the line
            motors.on(left_speed=-20, right_speed=0)
        elif direction == "left":
            # Same as above but for the left colour sensor
            motors.on(left_speed=0, right_speed=-20)
        elif direction == "forward":
            # Move forward when both colour sensors are not detecting black
            motors.on(left_speed=-20, right_speed=-20)
        elif direction == "intersectionRight":
            motors.on_for_degrees(left_speed=-10, right_speed=-10, degrees=360)
            while True:
                motors.on(left_speed=-10, right_speed=0)
                if cl_4.color == ColorSensor.COLOR_BLACK:
                    motors.on_for_degrees(left_speed=0, right_speed=-10, degrees=20)
                    break
            # motors.on_for_seconds(left_speed=20, right_speed=20, seconds=1)
        elif direction == "intersectionLeft":
            motors.on_for_degrees(left_speed=0, right_speed=-20, degrees=90)
            # motors.on_for_seconds(left_speed=20, right_speed=20, seconds=1)
        else:
            # motors.off()
            # Otherwise, move forward when both colour sensors are detecting green
            motors.on(left_speed=-20, right_speed=-20)
    else:
        # If the ultrasonic sensor detects an object within 5cm, the robot will stop and display the distance on the screen
        motors.off()
    display.clear()
    distance = ultrasonic.distance_centimeters
    display.text_pixels("Object is {}cm away".format(distance), x=10, y=30, clear_screen=False) # Ultrasonic debug
    display.text_pixels("{}".format(distance), x=10, y=30, clear_screen=False) # Ultrasonic debug
    display.update()
    # if distance < 5:
    #     avoidObstable() # Will have to be worked on to make sure the robot can get back to the line after avoiding the obstacle
