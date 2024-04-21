# Bluetooth
sudo bluetootchtl
- scan on
- pair XX:XX:XX:XX:XX:XX
- trust XX:XX:XX:XX:XX:XX
- exit
sudo rfcomm bind /dev/rfcomm1 00:21:09:00:21:87
rfcomm

# Python
sudo nano /etc/pip.conf
[global]
break-system-packages = true

# DHT
sudo pip3 install adafruit-circuitpython-dht