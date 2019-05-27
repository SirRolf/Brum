import motor as MotorControl
from stateMachine import *


MotorControl.turnLeft(0.25)
MotorControl.turnRight(0.25)

while True:
    stateMachine.Update()
