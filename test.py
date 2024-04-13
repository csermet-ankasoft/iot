import bluetooth

sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect(("00:21:09:00:21:87", 1))
sock.send("hello!!")
sock.close()
