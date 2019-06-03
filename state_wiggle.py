import motor as MotorControl
from random import randint

class state_wiggle():
    def Act(self):
        MotorControl.turnLeft(0.25)
        MotorControl.turnRight(0.5)
        motorControl.turnleft(0.25)
    def Reason(self):
        if randint(0, 100) < 50:
            exit()
