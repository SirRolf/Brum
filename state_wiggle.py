import motor as MotorControl

class state_wiggle():
    def Act(self):
        MotorControl.turnLeft(0.25)
        MotorControl.turnRight(0.25)
    def Reason(self):
        if randint(0, 100) < 50:
            exit()
