import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac = [8,11,7,1,0,5,12,6]
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(24,GPIO.IN)

p = GPIO.PWM(21, 60)


p.start(0)
try:
    while True:
        k = int(input())
        p.ChangeDutyCycle(k)

finally:
    p.stop()
    GPIO.cleanup()




