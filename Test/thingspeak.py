import socket 
import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('METAS HONG KONG','aabbccddee')
if not wlan.isconnected():
     while not wlan.isconnected():
        time.sleep(1)
        print('wait...')
        pass

print('network config:', wlan.ifconfig())#getip
s = socket.socket()
#host = wlan.ifconfig()[0]
host = '184.106.153.149'
port = 80
s.connect([host,port])
'''s.bind([host,port])
s.listen(1)'''
while True:
   # c,addr = s.accept()
    s.send("GET /update?key=66Z4DZA8J7LXN99B&field3=1&field4=1&field1=1&field2=2&field5=5&field6=6 HTTP/1.1\r\n")
    s.send("Host: api.thingspeak.com\r\nAccept: */*\r\nUser-Agent: Mozilla/4.0 (compatible; esp8266 Lua; Windows NT 5.1)\r\n\r\n")
    time.sleep(15)
    #s.close()
    
