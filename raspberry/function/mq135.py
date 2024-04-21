import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
airQuality = AnalogIn(ads, ADS.P0)

def getAirQuality():
    try:
        airQuality = round(airQuality.value/32.767)
        print("Air Quality: ", )
    except RuntimeError as error:
        raise error.args[0]
    return airQuality

def status():
    try:
        getAirQuality()
    except Exception as error:
        raise error