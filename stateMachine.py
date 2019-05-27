import motor as MotorControl
import state_wander

class stateMachine(object):
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
        while isOn:
            _currentState.Reason()
            _currentState.Act()

    def AddState(stateId, State):
        _states.Add(stateId, State)
