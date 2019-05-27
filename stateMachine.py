import motor as MotorControl
from state_wander import *

class stateMachine():
    _states = {

    }

    _currentState = state_wander()

    isOn = True

    def SetState(stateId):
        if _states in _currentState.Keys():
            print "return"
            return
        _currentState = _states[stateId]

    def Update():
        while True:
            _currentState.Reason()
            _currentState.Act()

    def AddState(stateId, State):
        _states.Add(stateId, State)

    Update()
