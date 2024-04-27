import serial

arduinoBluetooth = serial.Serial("/dev/rfcomm1", baudrate=9600)

def __get_bluetooth(text):
    arduinoBluetooth.write(text)
    print("BluetoothSend: ", text)
    recieve = arduinoBluetooth.readline()
    print("BluetoothRecieved: ", recieve)

def get_humidty():
    __get_bluetooth(b'getHumidity')

def get_temperature():
    __get_bluetooth(b'getTemperature')

def get_airQuality():
    __get_bluetooth(b'getAirQuality')

def status():
    __get_bluetooth(b'status')
    print("\n")