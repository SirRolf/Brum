import motor as MotorControl
from state_wander import *
from state_wiggle import *
from state_stay import *
from state_backOff import *

class stateMachine():
    def __init__(self):
        self._states = {
            "wander" : state_wander(self),
            "wiggle" : state_wiggle(),
            "stay" : state_stay(self),
            "backOff" : state_backOff(self)
        }
        self._currentState = self._states["wander"]

    def SetState(self, stateId):
        if stateId in self._states:
            self._currentState = self._states[stateId]

    def Update(self):
        self._currentState.Act()
        self._currentState.Reason()

    def AddState(self, stateId, State):
        self._states.Add(stateId, State)
