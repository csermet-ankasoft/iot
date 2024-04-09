import gpiod
import time     
import spidev
from nrf24 import NRF24
from machine import Pin, SPI
from digitalio import DigitalInOut, Direction, Pull


pipes = (b'\xe1\xf0\xf0\xf0\xf0', b'\xd2\xf0\xf0\xf0\xf0')

spi = SPI(0, sck=Pin(6), mosi=Pin(7), miso=Pin(4))
csn = Pin(14, mode=Pin.OUT, value=1)
ce = Pin(17, mode=Pin.OUT, value=0)
radio = NRF24(spi, csn, ce, channel=100, payload_size=32)

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