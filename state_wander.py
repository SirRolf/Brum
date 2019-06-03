import motor as MotorControl
from random import *
from stateMachine import *

class state_wander():
    def __init__(self, stateMachine):
        self._stateMachine = stateMachine
        commands = [
        MotorControl.forward(random() * .5),
        MotorControl.backward(random() * .05),
        MotorControl.wait(random() * 1),
        exit()
        ]
    def Act(self):
        choise(commands)

    def Reason(self):
        pass
