import motor as MotorControl
from stateMachine import *

_stateMachine = stateMachine()

while True:
    _stateMachine.Update()
