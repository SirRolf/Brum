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
        [MotorControl.forward, .25, .5, [80,0,10,25,25]],
        [MotorControl.backward, .1, .2],
        [MotorControl.wait, 2, 3, [80,0,45,0,0]],
        [MotorControl.turnLeft, .2, .5, [80,0,0,0,0]],
        [MotorControl.turnRight, .2, .5, [80,0,0,0,0]]
        ]
        self.commandChances = [
        80,
        0,
        25,
        0,
        0
        ]
    def Act(self):
        # gets a random command
        command = RandomList(self.commands, self.commandChances)
        # runs the script inside the commands array and gives it random times
        command[0](random.uniform(command[1],command[2]))
        if command[3] is not None:
            self.commandChances = command[3]

    def Reason(self):
        if random.randint(1, 100) < 3:
            print("going to stay here for a bit")
            self._stateMachine.SetState("stay")
        # stops application if the distance of the sensor is lower then the value given
        if sensordetect() < 20:
            print("wall, backing off")
            self._stateMachine.SetState("backOff")
