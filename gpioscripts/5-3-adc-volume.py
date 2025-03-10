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
leds = [2, 3, 4, 17, 27, 22, 10, 9]

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial=1)
gpio.setup(comp, gpio.IN)
gpio.setup(crutch, gpio.IN)
gpio.setup(leds, gpio.OUT)

def adc2():
    val = 0
    for i in range(7, -1, -1):
        s = 2 ** i
        val += s
        bin = dectobin(val)
        gpio.output(dac, bin)
        time.sleep(0.006)
        if gpio.input(crutch) == 1:
            val -= s
    return val

def adc():
    for i in range(256):
        gpio.output(dac, dectobin(i))
        time.sleep(0.01)
        if gpio.input(crutch) == 1:
            return i
    return 255
            

try:
    led = [0] * 8
    while True:
        
        x = dectobin(adc2())
        
        for i in range(8):
            if x[i] == 1:
                for j in range(i, 8):
                    x[j] = 1

        gpio.output(leds, x)
        time.sleep(0.01)

finally:
    gpio.output(dac, 0)
    gpio.output(troyka, 0)
    gpio.cleanup()