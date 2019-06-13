import motor as MotorControl
from stateMachine import *
from sensordetection import sensordetect


class state_backOff():
    def __init__(self, stateMachine):
        self._stateMachine = stateMachine
        self.isDone = False
    def Act(self):
        MotorControl.backward(1)
        MotorControl.wait(.2)
        MotorControl.turnLeft(.3)
        self.isDone = True
    def Reason(self):
        if self.isDone is True:
            self.isDone = False
            exit()
