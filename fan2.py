import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

IN1=20
IN2=21
ENA=16

GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(ENA,GPIO.OUT)
GPIO.output(IN1,GPIO.LOW)
GPIO.output(IN2,GPIO.LOW)

p=GPIO.PWM(ENA,1000)
p.start(0)

GPIO.output(IN1,GPIO.HIGH)
GPIO.output(IN2,GPIO.LOW)
p.ChangeDutyCycle(100)