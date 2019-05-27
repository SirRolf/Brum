import motor as MotorControl
from stateMachine import *

for x in 5:
    MotorControl.turnLeft(0.25)
    MotorControl.turnRight(0.25)
