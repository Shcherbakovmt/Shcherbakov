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

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
dac = [8,11,7,1,0,5,12,6]
GPIO.setup(dac, GPIO.OUT)
T = float(input())

try:
    while True:
            
        for volt in range(255):
            bin_i = ten_to_bin(volt)
            for j in range(len(dac)):
                    GPIO.output(dac[j], int(bin_i[j]))
            time.sleep(float(T/512))
        for volt in range(255):
            bin_i = ten_to_bin(255 - volt)
            for j in range(len(dac)):
                    GPIO.output(dac[j], int(bin_i[j]))
            time.sleep(float(T/512))
            
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()