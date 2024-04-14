import bluetooth

sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect(("00:21:09:00:21:87", 1))
sock.send("send")
sock.close()

server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
size = 1024
server_sock.bind(("00:21:09:00:21:87",1))
server_sock.listen(1)

try:
	client, clientInfo = server_sock.accept()
	while 1:
		data = client.recv(size)
		if data:
			print(data)
			client.send(data) # Echo back to client
except:	
	print("Closing socket")
	client.close()
	server_sock.close()
