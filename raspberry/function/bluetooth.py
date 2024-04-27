import serial

arduinoBluetooth = serial.Serial("/dev/rfcomm1", baudrate=9600, timeout=2)

def __get_bluetooth(text):
    arduinoBluetooth.write(text)
    print("Waiting for Bluetooth " + text.decode('UTF-8') + " response...")
    recieve = arduinoBluetooth.read_until(b';').decode('UTF-8')
    return recieve[:-1]

def get_humidty():
    return __get_bluetooth(b'getHumidity')

def get_temperature():
    return __get_bluetooth(b'getTemperature')

def get_airQuality():
    return __get_bluetooth(b'getAirQuality')

def status():
    __get_bluetooth(b'status')
    print("")