import serial

arduinoBluetooth = serial.Serial("/dev/rfcomm1", baudrate=9600)

def get_bluetooth(text):
    arduinoBluetooth.write(text)
    print("BluetoothSend: ", text)
    recieve = arduinoBluetooth.readline()
    print("BluetoothRecieved: ", recieve)

def get_humidty():
    get_bluetooth(b'getHumidity')

def get_temperature():
    get_bluetooth(b'getTemperature')

def get_airQuality():
    get_bluetooth(b'getAirQuality')
