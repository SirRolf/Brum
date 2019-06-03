import motor as MotorControl
import random
from stateMachine import *

class state_wander():
    def __init__(self, stateMachine):
        self._stateMachine = stateMachine
        commands = [
        MotorControl.forward(random.random() * 6),
        MotorControl.backward(random.random() * 1),
        MotorControl.wait(random.random() * 10),
        exit()
        ]
    def Act(self):
        random.choise(commands)

    def Reason(self):
        pass
