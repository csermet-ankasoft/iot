import bluetooth
  
nearby_devices = bluetooth.discover_devices()
for bdaddr in nearby_devices:
    print(str(bluetooth.lookup_name( bdaddr )) + " [" + str(bdaddr) + "]")

sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect(("00:21:09:00:21:87", 1))
sock.send("hello!!")
sock.close()
