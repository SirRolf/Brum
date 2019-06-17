import motor as MotorControl
from stateMachine import *
import signal

_stateMachine = stateMachine()

class init():
    def signal_handler(sig, frame):
        print('You pressed Ctrl+C!')
        MotorControl.motorsOff()
        exit()

    def run_program():
        while True:
            _stateMachine.Update()
            signal.signal(signal.SIGINT, signal_handler)
            print('Press Ctrl+C')
    run_program()
