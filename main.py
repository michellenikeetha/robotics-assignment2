#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor, UltrasonicSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick.
ev3 = EV3Brick()

obstacle_sensor = InfraredSensor(Port.S2)

# Initialize the motors on Port B and Port C.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the DriveBase with the motors and wheel specifications.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

ev3.speaker.beep()

while True:
    # Begin driving forward at 200 millimeters per second.
    robot.drive(200, 0)

    # Wait until an obstacle is detected. This is done by repeatedly
    # doing nothing (waiting for 10 milliseconds) while the measured
    # distance is still greater than 300 mm.

    # Drive backward for 300 millimeters.
    robot.straight(300)

    # # Turn around by 120 degrees
    # robot.turn(120)

    while obstacle_sensor.distance() < 200:
        robot.stop()

    

# Drive forward at 200 mm/s.
# robot.drive(200, 0)

# # Let the robot drive straight for 3 seconds (3000 milliseconds).
# ev3.speaker.beep()
# wait(3000)

# # Stop the robot.
# robot.stop()
# ev3.speaker.beep()