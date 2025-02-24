import RPi.GPIO as gpio

def dectobin(a):
    return ([int(i) for i in bin(a)[2:].zfill(8)])

gpio.setmode(gpio.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
gpio.setup(dac, gpio.OUT)


try:
    while True:
        print("waiting for a 0-255 number input//q for quitting the cycle")
        a = input()
        if a == "q":
            break
        else:
            a = int(a)
        gpio.output(dac, dectobin(a))
        print(f"voltage is {3.3*a/256}")

except ValueError:
    print("not an int//<0")
except TypeError:
    print("the number was not a number")
except RuntimeError:
    print("the number was greater than 255")

finally:
    print("\ncleaning up...")
    gpio.output(dac, 0)
    gpio.cleanup()