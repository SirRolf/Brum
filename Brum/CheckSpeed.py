from sensordetection import sensordetect
import motor as MotorControl

def CheckSpeed():
    context = 0
    firstCheck = sensordetect()
    MotorControl.forward(.5)
    secondCheck = sensordetect()
    context = secondCheck - firstCheck
    context = context * 2
    print("speed is" + context + "cm/s")
    return context
