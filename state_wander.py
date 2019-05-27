import motor as MotorControl
from random import randint
from stateMachine import *

class state_wander():
    def Act(self):
        MotorControl.forward(.1)
    def Reason(self):
        if randint(0, 100) < 10:
            stateMachine.SetState(wiggle)
