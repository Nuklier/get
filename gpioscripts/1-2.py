import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

gpio.setup(20, gpio.OUT)

c = 0
while True:
    gpio.output(20, c % 2)
    time.sleep(1)
    c += 1
