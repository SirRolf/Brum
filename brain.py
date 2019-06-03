import motor as MotorControl
from stateMachine import *

_stateMachine = stateMachine()
class init():
    while True:
        _stateMachine.Update()
