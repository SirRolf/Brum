import motor as MotorControl
import state
from random import randint

class state_wander():
    def Act(self):
        MotorControl.forward(.1)
    def Reason(self):
        if randint(0, 100) < 1:
            exit()
