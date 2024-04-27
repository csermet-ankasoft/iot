import serial

arduinoBluetooth = serial.Serial("/dev/rfcomm1", baudrate=9600)

def __get_bluetooth(text):
    arduinoBluetooth.write(text)
    #print("BluetoothSend: ", text.decode('UTF-8'))
    print("Waiting for Bluetooth " + text + " response...")
    recieve = arduinoBluetooth.read_until(b';').decode('UTF-8')
    #print("BluetoothRecieved: ", recieve)
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