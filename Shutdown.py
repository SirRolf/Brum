import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT)
gpio.setup(22, gpio.OUT)
gpio.setup(23, gpio.OUT)
gpio.setup(24, gpio.OUT)

gpio.output(17,False)
gpio.output(22,False)
gpio.output(23,False)
gpio.output(24,False)
gpio.cleanup()
