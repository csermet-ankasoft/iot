import socket
import time
from time import sleep
import machine

GPIO_PIN_9 = machine.Pin(9)
pwm9 = machine.PWM(GPIO_PIN_9)
pwm9.freq(25000)
