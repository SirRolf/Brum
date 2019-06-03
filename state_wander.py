import motor as MotorControl
import random
from stateMachine import *

class state_wander():
    def __init__(self, stateMachine):
        self._stateMachine = stateMachine
        self.commands = [
        MotorControl.forward,
        MotorControl.backward,
        MotorControl.wait,
        MotorControl.turnLeft,
        MotorControl.turnRight
        ]
    def Act(self):
        random.choice(self.commands)(.5)

    def Reason(self):
        if random.randint(0, 100) < 30:
            exit()
