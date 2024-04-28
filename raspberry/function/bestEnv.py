def temp(temp):
    temp = float(temp)
    if temp >= 21.0 and temp < 25.0:
        return 5
    elif temp >= 20.0 and temp < 21.0 or temp >= 25.0 and temp < 26.0:
        return 4
    elif temp >= 18.0 and temp < 20.0 or temp >= 26.0 and temp < 28.0:
        return 3
    elif temp >= 14.0 and temp < 18.0 or temp >= 28.0 and temp < 32.0:
        return 2
    elif temp >= 8.0 and temp < 14.0 or temp >= 32.0 and temp < 38.0:
        return 1
    else:
        return 0
    
def humidity(humidity):
    humidity = float(humidity)
    if humidity >= 40 and humidity < 60:
        return 5
    elif humidity >= 35 and humidity < 40 or humidity >= 60.0 and humidity < 65:
        return 4
    elif humidity >= 30 and humidity < 35 or humidity >= 65.0 and humidity < 70:
        return 3
    elif humidity >= 25 and humidity < 30 or humidity >= 70.0 and humidity < 75:
        return 2
    elif humidity >= 20 and humidity < 25 or humidity >= 75.0 and humidity < 80:
        return 1
    else:
        return 0
    
def airQuality(airQuality):
    airQuality = int(airQuality)
    if airQuality >= 0 and airQuality < 10:
        return 5
    elif airQuality >= 10 and airQuality < 15:
        return 4
    elif airQuality >= 15 and airQuality < 20:
        return 3
    elif airQuality >= 20 and airQuality < 25:
        return 2
    elif airQuality >= 25 and airQuality < 40:
        return 1
    else:
        return 0
