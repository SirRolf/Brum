import motor as MotorControl
from stateMachine import *

_stateMachine = stateMachine()

MotorControl.turnLeft(0.25)
MotorControl.turnRight(0.25)

while True:
    _stateMachine.Update()
