import motor as MotorControl
import random
from sensordetection import sensordetect
from stateMachine import *

class state_wander():
    def __init__(self, stateMachine):
        self._stateMachine = stateMachine
        # put your commands here
        self.commands = [
        [MotorControl.forward, .2, .4],
        [MotorControl.backward, .1, .2],
        [MotorControl.wait, 2, 3],
        [MotorControl.turnLeft, .2, .5],
        [MotorControl.turnRight, .2, .5]
        ]
    def Act(self):

        # gets a random command
        command = random.choices(self.commands, weights=[0.1, 0.1, 0.6, 0.1, 0.1], k=1)
        # runs the script inside the commands array and gives it random times
        command[0](random.uniform(command[1],command[2]))

    def Reason(self):
        # stops application if the distance of the sensor is lower then the value given
        if sensordetect() < 10:
            print("stopping cus of distance")
            exit()
