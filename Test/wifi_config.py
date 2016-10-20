import socket
import machine
import time
import network

def wifi_handle(list):
    list = list.decode('utf-8')
    e = list.find('HTTP')
    list = list[:e-1]
    e = list.find('&')
    if e==-1:
		pass
    else:
		ssid = list[11:e]
		ssid = ssid.replace('+',' ')
		pwd = list[e+5:]
		f = open('wifi.py','w+')
		f.write('ssid="'+ssid+'"')
		f.write('\n')
		f.write('pwd="'+pwd+'"')
		f.close()
		machine.reset()
		# sta = network.WLAN(network.STA_IF)
		# sta.active(True)
		# sta.connect(ssid,pwd)
		# print(ssid+pwd)
		# while not sta.isconnected():
			# print('please wait...')
			# time.sleep(1)
		# print(sta.ifconfig())
   
ap = network.WLAN(network.AP_IF)
ap.active(True)
host = ap.ifconfig()[0]
port = 80
s = socket.socket()
s.bind([host,port])
s.listen(1)
buf = '''
	<!DOCTYPE html>
	<html><head><meta http-equiv=Content-Type content='text/html;charset=utf-8'></head>
	<body><h1>Wifi Web Server</h1>
	<form method = 'get' action='http://192.168.4.1'>
	ssid:<input type='text' name='ssid'></input><br>
	pwd:<input type='password' name='pwd'></input><br>
	<button type='submit'>save</button>
	</form>
	</body>
	<html>
'''

while True:
	c,addr = s.accept()
	wifi_handle(c.recv(1024))
	c.sendall(buf)
	time.sleep(5)
	c.close
