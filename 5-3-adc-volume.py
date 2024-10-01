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
leds = [2,3,4,17,27,22,10,9]
GPIO.setup(leds, GPIO.OUT)

def adc():
    number = 0
    s = [0,0,0,0,0,0,0,0]
    for i in range(8):
        s[i] = 1
        GPIO.output(dac, s)
        time.sleep(0.001)
        if GPIO.input(comp) == 0:
            number += s[i]*( 2**(7-i) )
            continue
        if GPIO.input(comp) == 1:
            s[i] = 0
            number += s[i]*( 2**(7-i) )
            continue
    return number*3.3/255
        

try:
    while True:
        voltage = adc()/3.3
        for i in range(8):
            if (i+1)/8 < voltage:
                GPIO.output(leds[i], 1)
            else:
                GPIO.output(leds[i],0)
finally:
    GPIO.cleanup()


