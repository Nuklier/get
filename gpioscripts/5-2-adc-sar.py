import RPi.GPIO as gpio
import time

def dectobin(a):
    return ([int(i) for i in bin(a)[2:].zfill(8)])

def bintodec(a):
    x = 0
    for i in range(len(a)):
        x = x + a[i] * 2 ** i
    return x

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
    val = 0
    for i in range(7, -1, -1):
        s = 2 ** i
        val += s
        bin = dectobin(val)
        gpio.output(dac, bin)
        time.sleep(0.007)
        if gpio.input(crutch) == 1:
            val -= s
    return val
            

try:
    while True:
        x = adc()
        print(f"{x*3.3/255} volts, {x}")
        time.sleep(0.1)

finally:
    gpio.output(dac, 0)
    gpio.output(troyka, 0)
    gpio.cleanup()