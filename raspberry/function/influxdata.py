import time
import influxdbToken
from influxdb_client_3 import InfluxDBClient3, Point

def writeWithLocation(arduino_temp, arduino_humidity, arduino_air_quality, arduino_score, raspberry_temp, raspberry_humidity, raspberry_air_quality, raspberry_score):
  client = InfluxDBClient3(host=influxdbToken.host, token=influxdbToken.token , org=influxdbToken.org)
  database = influxdbToken.database

  try:
    arduino_temp = float(arduino_temp)
  except ValueError:
    arduino_temp = 0.0

  try:
    arduino_humidity = float(arduino_humidity)
  except ValueError:
    arduino_humidity = 0.0
  
  try:
    arduino_air_quality = int(arduino_air_quality)
  except ValueError:
    arduino_air_quality = 0

  try:
    raspberry_temp = float(raspberry_temp)
  except ValueError:
    raspberry_temp = 0.0

  try:
    raspberry_humidity = float(raspberry_humidity)
  except ValueError:
    raspberry_humidity = 0.0

  try:
    raspberry_air_quality = int(raspberry_air_quality)
  except ValueError:
    raspberry_air_quality = 0    


  data = (
    Point("withLocation")
    .tag("location", "Arduino")
    .field("temperature", arduino_temp)
    .field("humidity",  arduino_humidity)
    .field("air_quality", arduino_air_quality)
    .field("score", arduino_score),
    Point("withLocation")
    .tag("location", "Raspberry")
    .field("temperature", raspberry_temp)
    .field("humidity", raspberry_humidity)
    .field("air_quality", raspberry_air_quality)
    .field("score", raspberry_score)
  )
  client.write(database=database, record=data)

def writeWithoutLocationData(arduino_temp, arduino_humidity, arduino_air_quality, arduino_score, raspberry_temp, raspberry_humidity, raspberry_air_quality, raspberry_score):
  client = InfluxDBClient3(host=influxdbToken.host, token=influxdbToken.token , org=influxdbToken.org)
  database = influxdbToken.database


  try:
    arduino_temp = float(arduino_temp)
  except ValueError:
    arduino_temp = 0.0

  try:
    arduino_humidity = float(arduino_humidity)
  except ValueError:
    arduino_humidity = 0.0
  
  try:
    arduino_air_quality = int(arduino_air_quality)
  except ValueError:
    arduino_air_quality = 0

  try:
    raspberry_temp = float(raspberry_temp)
  except ValueError:
    raspberry_temp = 0.0

  try:
    raspberry_humidity = float(raspberry_humidity)
  except ValueError:
    raspberry_humidity = 0.0

  try:
    raspberry_air_quality = int(raspberry_air_quality)
  except ValueError:
    raspberry_air_quality = 0    

  data = (
    Point("withoutLocation")
    .field("arduino_temp", arduino_temp)
    .field("arduino_humidity", arduino_humidity)
    .field("arduino_air_quality", arduino_air_quality)
    .field("arduino_score", arduino_score)
    .field("raspberry_temp", raspberry_temp)
    .field("raspberry_humidity", raspberry_humidity)
    .field("raspberry_air_quality", raspberry_air_quality)
    .field("raspberry_score", raspberry_score)
  )
  client.write(database=database, record=data)


def writeData(arduino_temp, arduino_humidity, arduino_air_quality, arduino_score, raspberry_temp, raspberry_humidity, raspberry_air_quality, raspberry_score):
  writeWithLocation(arduino_temp, arduino_humidity, arduino_air_quality, arduino_score, raspberry_temp, raspberry_humidity, raspberry_air_quality, raspberry_score)
  time.sleep(10)
  writeWithoutLocationData(arduino_temp, arduino_humidity, arduino_air_quality, arduino_score, raspberry_temp, raspberry_humidity, raspberry_air_quality, raspberry_score)

def status():
  client = InfluxDBClient3(host=influxdbToken.host, token=influxdbToken.token , org=influxdbToken.org)
  database = influxdbToken.database

  query = "SELECT * FROM 'withLocation' WHERE time >= now() - interval '1 hours'"

  # Execute the query
  table = client.query(query=query, database=database, language='sql')

  # Convert to dataframe
  table.to_pandas().sort_values(by="time")
