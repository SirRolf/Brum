from sensordetection import sensordetect
import motor as MotorControl

def CheckSpeed():
    context = 0
    firstCheck = sensordetect()
    MotorControl.forward(1)
    secondCheck = sensordetect()
    context = secondCheck - firstCheck
    print("speed is" + context + "cm/s")
    return context
