from tkinter import *
import RPi.GPIO as GPIO
import time

pino_led = 32

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pino_led, GPIO.OUT)
pwm = GPIO.PWM(pino_led, 100)
pwm.start(0)

# print("Espera 2 segundos")
# time.sleep(2)

# try:    
#     while(True):            
#         print("Led Apagado!")
#         pwm.ChangeDutyCycle(50)
#         time.sleep(5)
#         print("Led Aceso!")
#         pwm.ChangeDutyCycle(50)
#         time.sleep(5)
# finally:
#     GPIO.cleanup()




class App:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        scale = Scale(frame, from_=0, to=180,
              orient=HORIZONTAL, command=self.update)
        scale.grid(row=0)


    def update(self, angle):
        duty = float(angle) / 10.0 + 2.5
        pwm.ChangeDutyCycle(duty)



root = Tk()
root.title("Automação com Raspberry")
root.geometry("478x280")

app = App(root)

# Execute Tkinter
root.mainloop()
