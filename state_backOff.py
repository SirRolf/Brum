import motor as MotorControl
from stateMachine import *
from sensordetection import sensordetect


class state_backOff():
    def __init__(self, stateMachine):
        self._stateMachine = stateMachine
        isDone = False
    def Act(self):
        MotorControl.backward(1)
        if sensordetect() < 30:
            MotorControl.wait(.5)
            MotorControl.turnLeft(.5)
            isDone = True
    def Reason(self):
        if isDone is True:
            isDone = False
            exit()
