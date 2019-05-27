import motor as MotorControl
from state_wander import *

class stateMachine():
    def __init__(self):
        self._currentState = state_wander()
        self._states = {

        }

    def SetState(self, stateId):
        if stateId in self._states.Keys():
            return
        self._currentState = self._states[stateId]

    def Update(self):
        self._currentState.Reason()
        self._currentState.Act()

    def AddState(self, stateId, State):
        self._states.Add(stateId, State)

    while True:
        Update()
