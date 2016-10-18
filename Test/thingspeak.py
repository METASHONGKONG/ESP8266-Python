import socket 
import network
import time

wlan = network.WLAN(network.STA_IF)
if not wlan.isconnected():
     wlan.connect('Mr Xiao','12344321')
     while not wlan.isconnected():
        print('wait...')
        pass
s = socket.socket()
#host = wlan.ifconfig()[0]
host = '184.106.153.149'
port = 80
s.connect([host,port])
'''s.bind([host,port])
s.listen(1)'''
while True:
   # c,addr = s.accept()
    s.send("GET /update?key=SNF4N3W61JJ6ZXG4&field3=1&field4=1 HTTP/1.1\r\n")
    s.send("Host: api.thingspeak.com\r\nAccept: */*\r\nUser-Agent: Mozilla/4.0 (compatible; esp8266 Lua; Windows NT 5.1)\r\n\r\n")
    time.sleep(15)
    #s.close()