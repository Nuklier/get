import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

gpio.setup(21, gpio.OUT)
gpio.setup(3, gpio.OUT)


p = gpio.PWM(21, 60)
p1 = gpio.PWM(3, 60)
p.start(0)
p1.start(0)
try:
    while True:
        a = float(input("pwm duty cycle value:"))
        p.ChangeDutyCycle(a)
        p1.ChangeDutyCycle(a)
        print(f"voltage is {3.3*a/100}")


finally:
    gpio.output(21, 0)
    gpio.output(3, 0)
    gpio.cleanup()