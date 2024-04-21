import influxdbToken
from influxdb_client_3 import InfluxDBClient3, Point

def writeData(temp, humidity, air_quality, location):
  client = InfluxDBClient3(host=influxdbToken.host, token=influxdbToken.token , org=influxdbToken.org)
  database = influxdbToken.database

  data = (
    Point("iot")
    .tag("location", location)
    .field("temp", temp)
    .field("humidity", humidity)
    .field("air_quality", air_quality)
  )
  client.write(database=database, record=data)

  print("Influxdb Write Completed.")

def status():
  client = InfluxDBClient3(host=influxdbToken.host, token=influxdbToken.token , org=influxdbToken.org)
  database = influxdbToken.database

  query = "SELECT * FROM 'iot' WHERE time >= now() - interval '1 hours'"

  # Execute the query
  table = client.query(query=query, database=database, language='sql') )

  # Convert to dataframe
  df = table.to_pandas().sort_values(by="time")
  print(df)
