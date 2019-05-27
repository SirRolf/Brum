import motor as MotorControl
import state

class state_wander(State):
    def Act():
        MotorControl.turnRight(1)
