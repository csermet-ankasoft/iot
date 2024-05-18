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

        time.sleep(20)
        logger.info("Sleeping for 20 seconds.")
        
        
        predict = functions.Predict()

        raspberry_predict_temp = predict[0][0]
        raspberry_predict_humidity = predict[0][2]
        arduino_predict_temp = predict[0][1]
        arduino_predict_humidity = predict[0][3]

        raspberry_predict_score = functions.EnvScore(raspberry_predict_temp, raspberry_predict_humidity, raspberry_air_quality)
        arduino_predict_score = functions.EnvScore(arduino_predict_temp, arduino_predict_humidity, arduino_air_quality)
        current_diff_score = arduino_score - raspberry_score
        predict_diff_score = arduino_predict_score - raspberry_predict_score

        diff_score = max(current_diff_score, predict_diff_score)
        logger.info("Current Diff Score: " + str(current_diff_score) + " Predict Diff Score: " + str(predict_diff_score))

        fan_speed = functions.CalculateFanSpeed(diff_score)
        bluetooth.set_fanSpeed(fan_speed)

        lcd.writeLCD("PT:" + str(round(raspberry_predict_temp, 1)) + " PH:" + str(round(raspberry_predict_humidity)) + " F:" + str(fan_speed) , "PT:" + str(round(arduino_predict_temp, 1)) + " PH:" + str(round(arduino_predict_humidity)) + " S:" + str(round(diff_score, 1)))
        logger.info("PT:" + str(round(raspberry_predict_temp, 1)) + " PH:" + str(round(raspberry_predict_humidity)) + " F:" + str(fan_speed) + "  PT:" + str(round(arduino_predict_temp, 1)) + " PH:" + str(round(arduino_predict_humidity)) + " S:" + str(diff_score))
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
        time.sleep(10)