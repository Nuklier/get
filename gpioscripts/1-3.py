import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

gpio.setup(20, gpio.OUT)
gpio.setup(21, gpio.IN)

a = 0
a = gpio.input(21)
gpio.output(20, a)
