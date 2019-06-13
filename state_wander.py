import motor as MotorControl
import random
from sensordetection import sensordetect
from stateMachine import *
from listPicker import RandomList

class state_wander():
    def __init__(self, stateMachine):
        self._stateMachine = stateMachine
        # put your commands here
        self.commands = [
        [MotorControl.forward, .2, .4, [60,0,10,25,25]],
        [MotorControl.backward, .1, .2],
        [MotorControl.wait, 2, 3, [60,0,25,10,10]],
        [MotorControl.turnLeft, .2, .5, [60,0,10,25,25]],
        [MotorControl.turnRight, .2, .5, [60,0,10,25,25]]
        ]
        self.commandChances = [
        60,
        0,
        25,
        10,
        10
        ]
    def Act(self):
        # gets a random command
        command = RandomList(self.commands, self.commandChances)
        # runs the script inside the commands array and gives it random times
        command[0](random.uniform(command[1],command[2]))
        if command[3] is not None:
            ChangeList(command[3])

    def Reason(self):
        # stops application if the distance of the sensor is lower then the value given
        if sensordetect() < 30:
            print("going to stay")
            self._stateMachine.SetState("stay")

    def ChangeList(self, newChances):
        self.commandChances = newChances
