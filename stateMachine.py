import motor as MotorControl

_states = {

}

_currentState = "somthing"

isOn = True

def SetState(stateId):
    if _states in _currentState.Keys():
        print "return"
        return
    _currentState = _states[stateId]

def Update():
    while isOn:
        _currentState.Act()

def AddState(stateId, State):
    _states.Add(stateId, State)
