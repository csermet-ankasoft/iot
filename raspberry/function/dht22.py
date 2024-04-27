import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT22(board.D18)

def get_temperature():
    try:
        temp = dhtDevice.temperature
        print("Temperature: {:.1f} C".format(temp))
    except RuntimeError as error:
        raise error.args[0]
    except Exception as error:
        dhtDevice.exit()
        raise error

    return temp

def get_humidity():
    try:
        humidity = dhtDevice.humidity
        print("Humidity: {:.1f}%".format(humidity))
    except RuntimeError as error:
        raise error.args[0]
    except Exception as error:
        dhtDevice.exit()
        raise error
    return humidity

def status():
    try:
        get_temperature()
        get_humidity()
        print("\n")
    except Exception as error:
        raise error