import time
import function.bluetooth as bluetooth
import function.dht22 as dht22
import function.influxdata as influxdata
import function.mq135 as mq135
import function.lcd as lcd
import function.functions as functions
import logging as log


log.basicConfig(filename='/home/caner/Project/iot/raspberry/iot.log', level=log.INFO, format='%(asctime)s %(levelname)-8s %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
logger = log.getLogger('iot')

logger.info("Prediction AI Model Loaded.")
functions.Init()
logger.info("Starting...\n")

while True:
    try:
        logger.info("Scanning...")
        lcd.writeLCD("Scanning", "")
        
        arduino_air_quality = bluetooth.get_airQuality()
        arduino_temp = bluetooth.get_temperature()
        arduino_humidity = bluetooth.get_humidty()
        arduino_score = functions.EnvScore(arduino_temp, arduino_humidity, arduino_air_quality)
        raspberry_air_quality = mq135.getAirQuality()
        raspberry_temp = dht22.get_temperature()
        raspberry_humidity = dht22.get_humidity()
        raspberry_score = functions.EnvScore(raspberry_temp, raspberry_humidity, raspberry_air_quality)
        functions.printScannedData(arduino_temp, arduino_humidity, arduino_air_quality, arduino_score, raspberry_temp, raspberry_humidity, raspberry_air_quality, raspberry_score)

        time.sleep(30)
        logger.info("Sleeping for 30 seconds.")
        
        predict = functions.Predict()
        lcd.writeLCD("PT:" + str(round(predict[0][0], 3)) + "  PH:" + str(round(predict[0][2], 3)), "PTemp:" + str(round(predict[0][1], 3)) + "  PHum:" + str(round(predict[0][3], 3)))
        logger.info("PT:" + str(round(predict[0][0], 3)) + "  PH:" + str(round(predict[0][2], 3)) + "PTemp:" + str(round(predict[0][1], 3)) + "  PHum:" + str(round(predict[0][3], 3)))
        time.sleep(10)
        
        logger.info("Writing to DB...")
        lcd.writeLCD("Writing to DB", "")
        influxdata.writeData(arduino_temp, arduino_humidity, arduino_air_quality, arduino_score, raspberry_temp, raspberry_humidity, raspberry_air_quality, raspberry_score)
        logger.info("DB Write Completed.\n")
        lcd.writeLCD("DB Write Completed", "")
        time.sleep(5)
    except Exception as error:
        logger.info("Error: " + str(error))
        lcd.writeLCD("Error:", str(error))
        bluetooth.reset()
        time.sleep(25)