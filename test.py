import RPi.GPIO as GPIO
def ten_to_dvoich(N):
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
GPIO.setmode(GPIO.BCM)
dac = [8,11,7,1,0,5,12,6]
GPIO.setup(dac, GPIO.OUT)

try:
    while(True):
        n = input()
        if n == "q":
            break
        if(not is_number(n)):
            print("Это не число или оно не целое")
            continue
        if int(n) < 0:
            print("Это отрицательное число")
            continue
        if int(n) > 255:
            print("Слишком много")
            continue
        
        
        if int(n) >= 0 and int(n) <= 255:
            number = ten_to_dvoich(int(n))

            for i in range(len(dac)):
                GPIO.output(dac[i], int(number[i]))
            print("Теоретическое значение напряжения: ", float(int(n) * 3.248/255), "В")
        else:
            continue


        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()