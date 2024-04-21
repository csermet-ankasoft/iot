import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT22(board.D18)

def get_temperature():
    try:
        temp = dhtDevice.temperature
    except RuntimeError as error:
        raise error.args[0]
    except Exception as error:
        dhtDevice.exit()
        raise error

    return temp

def get_humidity():
    try:
        humidity = dhtDevice.humidity
    except RuntimeError as error:
        raise error.args[0]
    except Exception as error:
        dhtDevice.exit()
        raise error
    return humidity