import RPi.GPIO as GPIO
import time



pino_led = 32
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(pino_led, GPIO.OUT)


try:
    
    while(True):            
        print("Led Apagado!")
        GPIO.output(pino_led, 0)
        time.sleep(5)
        print("Led Aceso!")
        GPIO.output(pino_led, 1 )
        time.sleep(5)
finally:
    GPIO.cleanup()

    # xpt2046



