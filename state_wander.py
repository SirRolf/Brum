import motor as MotorControl
import random
from stateMachine import *

class state_wander():
    def __init__(self, stateMachine):
        self._stateMachine = stateMachine
        commands = [
        MotorControl.forward,
        MotorControl.backward,
        MotorControl.wait
        ]
    def Act(self):
        random.choice(commands)(randomint(1,4))

    def Reason(self):
        if randint(0, 100) < 30:
            exit()
