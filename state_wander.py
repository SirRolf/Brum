import motor as MotorControl
import random
from stateMachine import *

class state_wander():
    def __init__(self, stateMachine):
        self._stateMachine = stateMachine
        # put your commands here
        self.commands = [
        [MotorControl.forward, .2, .4] * 3,
        [MotorControl.backward, .1, .2] * 1,
        [MotorControl.wait, 2, 3] * 4,
        [MotorControl.turnLeft, .2, .5] * 2,
        [MotorControl.turnRight, .2, .5] * 2
        ]
    def Act(self):
        # gets a random command
        command = random.choice(self.commands)
        # runs the script inside the commands array and gives it random times
        command[0](random.uniform(command[1],command[2]))
        print(command)

    def Reason(self):
        # little somthing so you won't get an infinite loop
        if random.randint(0, 100) < 10:
            exit()
