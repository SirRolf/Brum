import motor as MotorControl
from state_wander import *

class stateMachine():
    _states = {

    }

    _currentState = state_wander()

    while True:
        _currentState.Reason()
        _currentState.Act()

    def SetState(stateId):
        if _states in _currentState.Keys():
            print "return"
            return
        _currentState = _states[stateId]

    def AddState(stateId, State):
        _states.Add(stateId, State)
