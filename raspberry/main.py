import time
import function.bluetooth as bluetooth
import function.dht22 as dht22
import function.influxdata as influxdata
import function.mq135 as mq135
import function.lcd as lcd

print("Init Check Started.\n")

bluetooth.status()
lcd.status()
dht22.status()
mq135.status()
#influxdata.status()

print("Check Completed.\n")

time.sleep(2)

print("Starting...\n")

while True:
    try:
        print("Scanning...\n")
        arduino_airQuality = bluetooth.get_airQuality()
        arduino_temp = bluetooth.get_temperature()
        arduino_humidity = bluetooth.get_humidty()
        raspberry_airQuality = mq135.getAirQuality()
        raspberry_temp = dht22.get_temperature()
        raspberry_humidity = dht22.get_humidity()
        print("\nArduino Air Quality: ", arduino_airQuality)
        print("Arduino Temperature: ", arduino_temp)
        print("Arduino Humidity: ", arduino_humidity)
        print("Raspberry Air Quality: ", raspberry_airQuality)
        print("Raspberry Temperature: ", raspberry_temp)
        print("Raspberry Humidity: ", raspberry_humidity)
        print("\nScan Completed \n")
        lcd.writeLCD("T:" + str(raspberry_temp) + " H:" + str(raspberry_humidity) + " A:" + str(raspberry_airQuality) + " O", "T:" + str(arduino_temp) + " H:" + str(arduino_humidity) + " A:" + str(arduino_airQuality) + " K")
        #time.sleep(45)
        print("\nWriting to DB...")
        influxdata.writeData(arduino_temp, arduino_humidity, arduino_airQuality, raspberry_temp, raspberry_humidity, raspberry_airQuality)
        print("DB Write Completed.\n")
        lcd.writeLCD("DB Write Completed")
        time.sleep(1)
    except Exception as error:
        time.sleep(10)
        lcd.writeLCD("Error", str(error))