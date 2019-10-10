import motor as MotorControl
from random import randint

class state_wiggle():
    def Act(self):
        MotorControl.turnLeft(0.25)
        MotorControl.turnRight(0.5)
        MotorControl.turnLeft(0.25)
        exit()
    def Reason(self):
        pass
