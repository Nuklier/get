import RPi.GPIO as gpio
import time
import matplotlib.pyplot as plt
def dectobin(a):
    return ([int(i) for i in bin(a)[2:].zfill(8)])


dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13
crutch = 21

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT)
gpio.setup(leds, gpio.OUT)
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
        if gpio.input(comp) == 1:
            val -= s
    return val
            

try:
    start = time.time()
    data = []
    gpio.output(troyka, 1)
    x = 0
    while x < 211: # пока заряжается
        x = adc()
        data.append(x)
        gpio.output(leds, dectobin(x))
        # print(f"{x*3.3/255} volts, {x}")
    gpio.output(troyka, 0)
    while x > 169: # пока разряжается
        x = adc()
        data.append(x)
        gpio.output(leds, dectobin(x))
    finish = time.time()
    tm = round(finish - start, 3)
    print(f"experiment duration  is {tm} seconds")
    print(f"period is {round(tm / len(data), 3)} seconds")
    print(f"frequency is {round(1 / (tm / len(data)), 4)} hz")
    print(f"adc step is {3.3/256} volts")
    

finally:
    # gpio cleaning
    gpio.output(dac, 0)
    gpio.output(leds, 0)
    gpio.output(troyka, 0)
    gpio.cleanup()
    # dataing
    for i in data:
        i = i*3.3/256
    strdata = [str(i) for i in data]
    with open("data.txt", "w") as f:
        f.write("\n".join(strdata))

    plt.plot(data)
    
    plt.show()