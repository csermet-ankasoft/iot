import serial
import time

port = serial.Serial("/dev/rfcomm1", baudrate=9600) # reading and writing data from and to arduino serially.
                                                    # rfcomm0 -> this could be different

while True:
    print("DIGITAL LOGIC -- > SENDING...")
    port.write("send")
    rcv = port.readline()
    if rcv:
        print(rcv)
    time.sleep(3)
