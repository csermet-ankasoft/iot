import time
import function.bluetooth as bluetooth
import function.dht22 as dht22
import function.influxdata as influxdata
import function.mq135 as mq135
import function.lcd as lcd
import function.bestEnv as bestEnv
import logging as log

def Init():
    logger.info("Init Check Started.")

    bluetooth.status()
    lcd.status()
    dht22.status()
    mq135.status()
    influxdata.status()

    logger.info("Check Completed.\n")
    time.sleep(2)

def EnvScore(temp, humidity, air_quality):
    tempScore = bestEnv.temp(temp)
    humidityScore = bestEnv.humidity(humidity)
    airQualityScore = bestEnv.airQuality(air_quality)
    return (tempScore + humidityScore + airQualityScore) / 3

def printScannedData(arduino_temp, arduino_humidity, arduino_air_quality, arduino_score, raspberry_temp, raspberry_humidity, raspberry_air_quality, raspberry_score):
    logger.info("Arduino Air Quality: " + str(arduino_air_quality))
    logger.info("Arduino Temperature: " + str(arduino_temp))
    logger.info("Arduino Humidity: " + str(arduino_humidity))
    logger.info("Arduino Score: " + str(arduino_score))
    logger.info("Raspberry Air Quality: " + str(raspberry_air_quality))
    logger.info("Raspberry Temperature: " + str(raspberry_temp))
    logger.info("Raspberry Humidity: " + str(raspberry_humidity))
    logger.info("Raspberry Score: " + str(raspberry_score))
    logger.info("Scan Completed")
    lcd.writeLCD("T:" + str(raspberry_temp) + " H:" + str(raspberry_humidity) + " S:" + str("{:.1f}".format(raspberry_score)) + " O", "T:" + str(arduino_temp) + " H:" + str(arduino_humidity) + " S:" + str("{:.1f}".format(arduino_score)) + " K")

log.basicConfig(filename='/home/caner/Project/iot/raspberry/iot.log', level=log.INFO, format='%(asctime)s %(levelname)-8s %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
logger = log.getLogger('iot')
Init()
logger.info("Starting...\n")

while True:
    try:
        logger.info("Scanning...")
        lcd.writeLCD("Scanning", "")
        arduino_air_quality = bluetooth.get_airQuality()
        arduino_temp = bluetooth.get_temperature()
        arduino_humidity = bluetooth.get_humidty()
        arduino_score = EnvScore(arduino_temp, arduino_humidity, arduino_air_quality)
        raspberry_air_quality = mq135.getAirQuality()
        raspberry_temp = dht22.get_temperature()
        raspberry_humidity = dht22.get_humidity()
        raspberry_score = EnvScore(raspberry_temp, raspberry_humidity, raspberry_air_quality)

        printScannedData(arduino_temp, arduino_humidity, arduino_air_quality, arduino_score, raspberry_temp, raspberry_humidity, raspberry_air_quality, raspberry_score)
        logger.info("Writing to DB...")
        influxdata.writeData(arduino_temp, arduino_humidity, arduino_air_quality, arduino_score, raspberry_temp, raspberry_humidity, raspberry_air_quality, raspberry_score)
        logger.info("DB Write Completed.\n")
        lcd.writeLCD("DB Write Completed", "")
        logger.info("Sleeping for 46 seconds.")
        time.sleep(46)
    except Exception as error:
        logger.info("Error: " + str(error))
        lcd.writeLCD("Error", str(error))
        time.sleep(100)