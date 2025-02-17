import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.cleanup()
leds = [2, 3, 4, 17 ,27 ,22, 10, 9]
aux = [21, 20, 26, 16, 19, 25, 23, 24]

gpio.setup(aux, gpio.IN)
gpio.setup(leds, gpio.OUT)

while True:
    for i in range(8):
        t = gpio.input(aux[i])
        gpio.output(leds[i], t)
        gpio.output(leds[i], 0)
    
