import motor as MotorControl
import state
import random

class state_wander():
    def Act():
        MotorControl.forward(.1)
    def Reason():
        if passrandom.randint(1,101) < 20:
            exit()
