import time
import influxdbToken
from influxdb_client_3 import InfluxDBClient3, Point

def writeWithLocation(arduino_temp, arduino_humidity, arduino_air_quality, arduino_score, raspberry_temp, raspberry_humidity, raspberry_air_quality, raspberry_score):
  client = InfluxDBClient3(host=influxdbToken.host, token=influxdbToken.token , org=influxdbToken.org)
  database = influxdbToken.database

  data = (
    Point("withLocation")
    .tag("location", "Arduino")
    .field("temperature", float(arduino_temp))
    .field("humidity",  float(arduino_humidity))
    .field("air_quality", int(arduino_air_quality))
    .field("score", int(arduino_score)),
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

  data = (
    Point("withoutLocation")
    .field("arduino_temp", float(arduino_temp))
    .field("arduino_humidity", float(arduino_humidity))
    .field("arduino_air_quality", int(arduino_air_quality))
    .field("arduino_score", int(arduino_score))
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
  print("Influxdb Write Completed.")

def status():
  client = InfluxDBClient3(host=influxdbToken.host, token=influxdbToken.token , org=influxdbToken.org)
  database = influxdbToken.database

  query = "SELECT * FROM 'withLocation' WHERE time >= now() - interval '1 hours'"

  # Execute the query
  table = client.query(query=query, database=database, language='sql')

  # Convert to dataframe
  df = table.to_pandas().sort_values(by="time")
  print(df)
