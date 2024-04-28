import time
import function.bluetooth as bluetooth
import function.dht22 as dht22
import function.influxdata as influxdata
import function.mq135 as mq135
import function.lcd as lcd
import function.bestEnv as bestEnv
import logging as log

def Init():
    logger.info("Init Check Started.\n")

    bluetooth.status()
    lcd.status()
    dht22.status()
    mq135.status()
    influxdata.status()

    logger.info("Check Completed.\n")
    time.sleep(2)

def arduinoEnvScore(arduino_temp, arduino_humidity, raspberry_air_quality):
    tempScore = bestEnv.temp(arduino_temp)
    humidityScore = bestEnv.humidity(arduino_humidity)
    airQualityScore = bestEnv.airQuality(raspberry_air_quality)
    return (tempScore + humidityScore + airQualityScore) / 3

def raspberryEnvScore(raspberry_temp, raspberry_humidity, raspberry_air_quality):
    tempScore = bestEnv.temp(raspberry_temp)
    humidityScore = bestEnv.humidity(raspberry_humidity)
    airQualityScore = bestEnv.airQuality(raspberry_air_quality)
    return (tempScore + humidityScore + airQualityScore) / 3

def printScannedData(arduino_temp, arduino_humidity, arduino_air_quality, arduino_score, raspberry_temp, raspberry_humidity, raspberry_air_quality, raspberry_score):
    logger.info("\nArduino Air Quality: ", arduino_air_quality)
    logger.info("Arduino Temperature: ", arduino_temp)
    logger.info("Arduino Humidity: ", arduino_humidity)
    logger.info("Arduino Score: ", arduino_score)
    logger.info("Raspberry Air Quality: ", raspberry_air_quality)
    logger.info("Raspberry Temperature: ", raspberry_temp)
    logger.info("Raspberry Humidity: ", raspberry_humidity)
    logger.info("Raspberry Score: ", raspberry_score)
    logger.info("\nScan Completed \n")
    lcd.writeLCD("T:" + str(raspberry_temp) + " H:" + str(raspberry_humidity) + " S:" + str(raspberry_score) + " O", "T:" + str(arduino_temp) + " H:" + str(arduino_humidity) + " S:" + str(arduino_score) + " K")

log.basicConfig(filename='/Project/iot/raspberry/iot.log', level=log.INFO)
logger = log.getLogger('iot')
Init()
logger.info("Starting...\n")
while True:
    try:
        logger.info("Scanning...\n")
        lcd.writeLCD("Scanning", "")
        raspberry_air_quality = bluetooth.get_airQuality()
        arduino_temp = bluetooth.get_temperature()
        arduino_humidity = bluetooth.get_humidty()
        arduino_score = arduinoEnvScore(arduino_temp, arduino_humidity, raspberry_air_quality)
        raspberry_air_quality = mq135.getAirQuality()
        raspberry_temp = dht22.get_temperature()
        raspberry_humidity = dht22.get_humidity()
        raspberry_score = raspberryEnvScore(raspberry_temp, raspberry_humidity, raspberry_air_quality)

        printScannedData(arduino_temp, arduino_humidity, raspberry_air_quality, arduino_score, raspberry_temp, raspberry_humidity, raspberry_air_quality, raspberry_score)
        time.sleep(36)
        logger.info("\nWriting to DB...")
        influxdata.writeData(arduino_temp, arduino_humidity, raspberry_air_quality, arduino_score, raspberry_temp, raspberry_humidity, raspberry_air_quality, raspberry_score)
        logger.info("DB Write Completed.\n")
        lcd.writeLCD("DB Write Completed", "")
        time.sleep(10)
    except Exception as error:
        time.sleep(100)
        logger.info("Error: ", error)
        lcd.writeLCD("Error", str(error))