import motor as MotorControl
import state
import random

class state_wander():
    def Act(self):
        MotorControl.forward(.1)
    def Reason(self):
        if passrandom.randint(1,101) < 20:
            exit()
