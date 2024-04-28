import time
import influxdbToken
from influxdb_client_3 import InfluxDBClient3, Point

def writeWithLocation(arduino_temp, arduino_humidity, arduino_air_quality, raspberry_temp, raspberry_humidity, raspberry_air_quality):
  client = InfluxDBClient3(host=influxdbToken.host, token=influxdbToken.token , org=influxdbToken.org)
  database = influxdbToken.database

  data = (
    Point("iot1")
    .tag("location", "Raspberry")
    .field("temp", raspberry_temp)
    .field("humidity", raspberry_humidity)
    .field("air_quality", raspberry_air_quality),
    Point("iot1")
    .tag("location", "Arduino")
    .field("temp", arduino_temp)
    .field("humidity", arduino_humidity)
    .field("air_quality", arduino_air_quality)
  )
  client.write(database=database, record=data)

def writeWithoutLocationData(arduino_temp, arduino_humidity, arduino_air_quality, raspberry_temp, raspberry_humidity, raspberry_air_quality):
  client = InfluxDBClient3(host=influxdbToken.host, token=influxdbToken.token , org=influxdbToken.org)
  database = influxdbToken.database

  data = (
    Point("iot2")
    .field("arduino_temp", arduino_temp)
    .field("arduino_humidity", arduino_humidity)
    .field("arduino_air_quality", arduino_air_quality)
    .field("raspberry_temp", raspberry_temp)
    .field("raspberry_humidity", raspberry_humidity)
    .field("raspberry_air_quality", raspberry_air_quality)
  )
  client.write(database=database, record=data)


def writeData(arduino_temp, arduino_humidity, arduino_air_quality, raspberry_temp, raspberry_humidity, raspberry_air_quality):
  writeWithLocation(arduino_temp, arduino_humidity, arduino_air_quality, raspberry_temp, raspberry_humidity, raspberry_air_quality)
  time.sleep(10)
  writeWithoutLocationData(arduino_temp, arduino_humidity, arduino_air_quality, raspberry_temp, raspberry_humidity, raspberry_air_quality)
  print("Influxdb Write Completed.")

def status():
  client = InfluxDBClient3(host=influxdbToken.host, token=influxdbToken.token , org=influxdbToken.org)
  database = influxdbToken.database

  query = "SELECT * FROM 'iot' WHERE time >= now() - interval '1 hours'"

  # Execute the query
  table = client.query(query=query, database=database, language='sql')

  # Convert to dataframe
  df = table.to_pandas().sort_values(by="time")
  print(df)
