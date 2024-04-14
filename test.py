import bluetooth

sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect(("00:21:09:00:21:87", 1))
sock.send("hello!!")
sock.close()

server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

server_sock.bind(("00:21:09:00:21:87",port))
server_sock.listen(1)

client_sock,address = server_sock.accept()
print("Accepted connection from " + str(address))

data = client_sock.recv(1024)
print("received [%s]" % data)

client_sock.close()
server_sock.close()
