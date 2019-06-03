import RPi.GPIO as gpio
import time

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)

def turnRight(duration):
    init()
    gpio.output(17,False)
    gpio.output(22,True)
    gpio.output(23,False)
    gpio.output(24,True)
    print("turnRight")
    time.sleep(duration)
    gpio.cleanup()

def turnLeft(duration):
    init()
    gpio.output(17,True)
    gpio.output(22,False)
    gpio.output(23,True)
    gpio.output(24,False)
    print("turnleft")
    time.sleep(duration)
    gpio.cleanup()

def backward(duration):
    init()
    gpio.output(17,True)
    gpio.output(22,False)
    gpio.output(23,False)
    gpio.output(24,True)
    print("backward")
    time.sleep(duration)
    gpio.cleanup()

def forward(duration):
    init()
    gpio.output(17,False)
    gpio.output(22,True)
    gpio.output(23,True)
    gpio.output(24,False)
    print("forward")
    time.sleep(duration)
    gpio.cleanup()

def wait(duration):
    init()
    gpio.output(17,False)
    gpio.output(22,False)
    gpio.output(23,False)
    gpio.output(24,False)
    print("wait")
    time.sleep(duration)
    gpio.cleanup()

def motorsOff():
    init()
    gpio.output(17,False)
    gpio.output(22,False)
    gpio.output(23,False)
    gpio.output(24,False)
    print("motorsOff")
    gpio.cleanup()
