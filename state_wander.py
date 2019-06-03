import motor as MotorControl
from random import *
from stateMachine import *

class state_wander():
    def __init__(self, stateMachine):
        self._stateMachine = stateMachine
        commands = [
        MotorControl.forward(random() * 6),
        MotorControl.backward(random() * 1),
        MotorControl.wait(random() * 10),
        exit()
        ]
    def Act(self):
        choise(commands)

    def Reason(self):
        pass
