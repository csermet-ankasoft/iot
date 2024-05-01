import serial

arduinoBluetooth = serial.Serial("/dev/rfcomm1", baudrate=9600, timeout=5)

def __get_bluetooth(text):
    arduinoBluetooth.write(text)
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

def reset():
    arduinoBluetooth.open()
    