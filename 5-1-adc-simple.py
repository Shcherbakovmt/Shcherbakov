import RPi.GPIO as GPIO
import time
def ten_to_bin(N):
    s = ''
    while N > 0:
        s += str(N%2)
        N = N//2
    s = s[::-1]
    s = (8- len(s))*"0" + s
    return s

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
troyka = 13
comp = 24
dac = [8,11,7,1,0,5,12,6]
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT)
GPIO.output(troyka, 1)


def adc():
    for i in range(255):
        binar = ten_to_bin(i)
        for j in range(8):
            GPIO.output(dac[j], int(binar[j]))
        time.sleep(0.005)
        if GPIO.input(comp) == 0:
            continue
        if GPIO.input(comp) == 1:
            return (3.3*i/255)
            break

try:
    while True:
        print(adc())
finally:
    GPIO.cleanup()


