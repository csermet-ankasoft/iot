import function.bluetooth as bluetooth
import function.dht22 as dht22
import function.influxdata as influxdata
import function.mq135 as mq135
import function.lcd as lcd
import function.bestEnv as bestEnv
import logging as log
import time
from tensorflow import keras 

logger = log.getLogger('iot')
prediction_model = keras.models.load_model("/home/caner/Project/iot/raspberry/iot_train.h5")

def Init():
    logger.info("Init Check Started.")

    while True:
        try:
            logger.info("Checking Bluetooth...")
            bluetooth.status()
            logger.info("Checking LCD...")
            lcd.status()
            logger.info("Checking DHT22...")
            dht22.status()
            logger.info("Checking MQ135...")
            mq135.status()
            logger.info("Checking InfluxDB...")
            influxdata.status()
            break
        except Exception as error:
            lcd.writeLCD("Error", str(error))
            logger.error("Error: " + str(error))
            logger.error("Check Failed.\n")
            bluetooth.reset()
            time.sleep(5)
            continue

    logger.info("Check Completed.")
    time.sleep(2)

def EnvScore(temp, humidity, air_quality):
    tempScore = bestEnv.temp(temp)
    humidityScore = bestEnv.humidity(humidity)
    airQualityScore = bestEnv.airQuality(air_quality)
    return round((tempScore + humidityScore + airQualityScore) / 3, 1)

def CalculateFanSpeed(score):
    if (score > 0 and score <= 0.5) :
        return 140
    elif score > 0.5 and score <= 1:
        return 170
    elif score > 1 and score <= 1.5:
        return 200
    elif score > 1.5 and score <= 2:
        return 220
    elif score > 2 and score <= 2.5:
        return 240
    elif score > 2.5:
        return 255
    else:
        return 100


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
    lcd.writeLCD("T:" + str(raspberry_temp) + " H:" + str(raspberry_humidity) + " S:" + str(raspberry_score), "T:" + str(arduino_temp) + " H:" + str(arduino_humidity) + " S:" + str(arduino_score))

def Predict():
    logger.info("Prediction Started.")
    lcd.writeLCD("Prediction Started", "")
    test_x = [[]]
    dataframe = influxdata.getLast10Row()
    for i in range(0, 10):
        test_x[0].append([dataframe.arduino_temp[i], dataframe.raspberry_temp[i], dataframe.arduino_humidity[i], dataframe.raspberry_humidity[i]])
    
    y_pred = prediction_model.predict(test_x)
    logger.info("Prediction Completed.")
    lcd.writeLCD("Prediction Completed", "")
    return y_pred