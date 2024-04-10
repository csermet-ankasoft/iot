import os, time
from influxdb_client_3 import InfluxDBClient3, Point

token = os.environ.get("INFLUXDB_TOKEN")
org = "Railgun"
host = "https://us-east-1-1.aws.cloud2.influxdata.com"

client = InfluxDBClient3(host=host, token=token, org=org)

database="IOT"

inside = (
  Point("my_test_point")
  .tag("location", "Inside")
  .field("temp", 33)
  .field("humidity", 87)
  .field("air_quality", 95)
)
client.write(database=database, record=inside)
time.sleep(1) # separate points by 1 second

outside = (
  Point("my_test_point")
  .tag("location", "Outside")
  .field("temp", 25)
  .field("humidity", 37)
  .field("air_quality", 195)
)
client.write(database=database, record=outside)
time.sleep(1) # separate points by 1 second

print("Completed.")
