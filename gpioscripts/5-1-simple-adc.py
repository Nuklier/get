import RPi.GPIO as gpio
import time

def dectobin(a):
    return ([int(i) for i in bin(a)[2:].zfill(8)])

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
crutch = 21

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial=1)
gpio.setup(comp, gpio.IN)
gpio.setup(crutch, gpio.IN)

def adc():
    for i in range(256):
        gpio.output(dac, dectobin(i))
        time.sleep(0.007)
        if gpio.input(crutch) == 1:
            return i
    return 255
            
            

try:
    while True:
        x = adc()
        print(f"{x*3.3/255} volts, {x}")
        time.sleep(0.1)

finally:
    gpio.output(dac, 0)
    gpio.output(troyka, 0)
    gpio.cleanup()