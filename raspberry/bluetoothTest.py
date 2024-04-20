import serial
import time

bluetooth = serial.Serial("/dev/rfcomm1", baudrate=9600)

while True:
    print("DIGITAL LOGIC -- > SENDING...")
    bluetooth.write(b'send')
    print("Writed")
    recieve = bluetooth.readline()
    print("recieved")
    if recieve:
        print(recieve)
    time.sleep(3)
