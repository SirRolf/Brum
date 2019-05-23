import RPI.GPIO as gpio
import time

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)

def forward(tf):
    init()
    gpio.output(17,False)
    gpio.output(22,True)
    gpio.output(23,False)
    gpio.output(24,True)
    time.sleep(tf)
    gpio.cleanup()

print "forward"
forward(4)
