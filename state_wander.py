import motor as MotorControl
import random
from stateMachine import *

commands = [
MotorControl.forward(random.random() * 6),
MotorControl.backward(random.random() * 1),
MotorControl.wait(random.random() * 10),
exit()
]

class state_wander():
    def __init__(self, stateMachine):
        self._stateMachine = stateMachine
    def Act(self):
        random.choice(commands)

    def Reason(self):
        pass
