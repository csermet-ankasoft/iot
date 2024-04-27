import time
import function.bluetooth as bluetooth
import function.dht22 as dht22
import function.influxdata as influxdata
import function.mq135 as mq135

print("Init Check Started.\n")

bluetooth.status()
dht22.status()
mq135.status()
#influxdata.status()

print("Check Completed.\n")

time.sleep(5)

print("Starting...")

while True:
    print("Scanning...")
    arduino_airQuality = bluetooth.get_airQuality()
    arduino_temp = bluetooth.get_temperature()
    arduino_humidity = bluetooth.get_humidty()
    raspberry_airQuality = mq135.getAirQuality()
    raspberry_temp = dht22.get_temperature()
    raspberry_humidity = dht22.get_humidity()
    print("Arduino Air Quality: ", arduino_airQuality)
    print("Arduino Temperature: ", arduino_temp)
    print("Arduino Humidity: ", arduino_humidity)
    print("Raspberry Air Quality: ", raspberry_airQuality)
    print("Raspberry Temperature: ", raspberry_temp)
    print("Raspberry Humidity: ", raspberry_humidity)
    #influxdata.writeData(raspberry_temp, raspberry_humidity, raspberry_airQuality, "Raspberry")    
    print("Scan Completed \n")
    time.sleep(10)