import RPi.GPIO as gpio
import time


gpio.setmode(gpio.BCM)

gpio.setup([2, 3, 4, 17, 27, 22, 10, 9], gpio.OUT)
leds = [2, 3, 4, 17, 27, 22, 10, 9]

for p in range(3):
    for i in leds:
        gpio.output(i, 1)
        time.sleep(0.2)
        gpio.output(i, 0)
gpio.output(leds, 0)
gpio.cleanup()