import motor as MotorControl
from random import randint
from stateMachine import *

self._stateMachine = stateMachine()

class state_wander():
    def Act(self):
        MotorControl.forward(.1)
    def Reason(self):
        if randint(0, 100) < 10:
            self._stateMachine.SetState(wiggle)
