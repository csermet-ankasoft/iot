import serial

arduinoBluetooth = serial.Serial("/dev/rfcomm1", baudrate=9600)

def __get_bluetooth(text):
    arduinoBluetooth.write(text)
    #print("BluetoothSend: ", text.decode('UTF-8'))
    recieve = arduinoBluetooth.readline().decode('UTF-8')
    #print("BluetoothRecieved: ", recieve)
    return recieve

def get_humidty():
    return __get_bluetooth(b'getHumidity')

def get_temperature():
    return __get_bluetooth(b'getTemperature')

def get_airQuality():
    return __get_bluetooth(b'getAirQuality')

def status():
    __get_bluetooth(b'status')
    print("")