import RPi.GPIO as GPIO
import time     
import spidev
from lib_nrf24 import NRF24

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pipes = [[0xE0, 0xE0, 0xF1, 0xF1, 0xE0], [0xF1, 0xF1, 0xF0, 0xF0, 0xE0]]

radio = NRF24(GPIO, spidev.SpiDev())
radio.begin(0, 17)

radio.setPayloadSize(32)
radio.setChannel(0x76)
radio.setDataRate(NRF24.BR_2MBPS)
radio.setPALevel(NRF24.PA_MIN)

radio.setAutoAck(True)
radio.enableDynamicPayloads()
radio.enableAckPayload()

radio.openWritingPipe(pipes[0])
radio.printDetails()

sendMessage = list("Hi..Arduino UNO")
while len(sendMessage) < 32:
    sendMessage.append(0)

while True:
    start = time.time()
    radio.write(sendMessage)
    print("Sent the message: {}".format(sendMessage))
    radio.startListening()

    while not radio.available(0):
        time.sleep(1/100)
        if time.time() - start > 2:
            print("Timed out.")  # print error message if the radio disconnected or not functioning anymore
            break

    radio.stopListening()     # close radio
    time.sleep(3)  # give delay of 3 seconds