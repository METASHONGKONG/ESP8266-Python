import socket
import machine
import time
import network
import ustruct

def wifi_handle(list):
	#find wifi ssid and password
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
		#Store information
		f = open('wifi.py','w+')
		f.write('ssid="'+ssid+'"')
		f.write('\n')
		f.write('pwd="'+pwd+'"')
		f.close()
		machine.reset()
        
b = ustruct.unpack('BBBB',machine.unique_id())
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='Metas_'+str(b[0]+b[1]+b[2]+b[3]),password='12345678')
host = ap.ifconfig()[0]
port = 80
s = socket.socket()
s.bind([host,port])
s.listen(1)
#web server
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
	c.sendall(buf)
	wifi_handle(c.recv(1024))
	time.sleep(5)
	c.close
