import function.bluetooth as bluetooth
import function.dht22 as dht22
import function.influxdata as influxdata
import function.mq135 as mq135

print("Init Check Started.")

bluetooth.status()
dht22.status()
mq135.status()
#influxdata.status()

print("Check Completed.")


