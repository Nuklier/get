import RPi.GPIO as gpio
import time

def dectobin(a):
    return ([int(i) for i in bin(a)[2:].zfill(8)])

gpio.setmode(gpio.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
gpio.setup(dac, gpio.OUT)

try:
    while True:
        for i in range(256):
            iter = dectobin(i)
            gpio.output(dac, iter)
            time.sleep(0.01)
        for i in range(255):
            iter = dectobin(255 - i)
            gpio.output(dac, iter)
            time.sleep(0.01)
finally:
    print("\ncleaning up...")
    gpio.output(dac, 0)
    gpio.cleanup()