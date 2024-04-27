import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c, address=0x48)

def getAirQuality():
    try:
        airQuality = AnalogIn(ads, ADS.P0)
        airQuality = round(airQuality.value/32767)
    except RuntimeError as error:
        raise error.args[0]
    return airQuality

def status():
    try:
        airQuality = getAirQuality()
        print("Air Quality: ", airQuality)
        print("")
    except Exception as error:
        raise error