'''
	NodeMcu(ESP8266) Dev
	Designed By Tom
	Copyright (c) 2016 METAS
'''
import network
import socket
from aREST import *
import ssd1306
from machine import Pin,I2C,ADC
import machine 


pin = [16,5,4,0,2,14,12,13,15,3,1,9,10] #GPIO->PIN
pin5 = Pin(pin[5],Pin.OUT)# init car control:stop
pin3 = Pin(pin[3],Pin.OUT)
pin5.value(0)
pin3.value(0)
pin8 = Pin(pin[8],Pin.OUT)#adc channel choose
pin8.value(1)
adc = ADC(0).read()
if adc > 800:
	import os
	os.remove('wifi.py')
dis_i2c = I2C(sda=Pin(pin[7]), scl=Pin(pin[6]))
display = ssd1306.SSD1306_I2C(128,32, dis_i2c, 60)
display.fill(0)
arest = aREST()#class

try:
	import wifi

except:
    import wifi_config
    
else:	
	wlan = network.WLAN(network.STA_IF)#station mode
	wlan.active(True)
	wlan.connect(wifi.ssid,wifi.pwd)#connect wlan
	while not wlan.isconnected():
		print('connecting...')
		time.sleep(1)
		display.text('please wait...',1,10,1)
		display.show()

	print('network config:', wlan.ifconfig())#getip
	display.fill(0)
	display.text(wlan.ifconfig()[0],1,10,1)
	display.show()
	s = socket.socket()#create socket
	host = wlan.ifconfig()#get hostname
	port = 80#listen port
	s.bind([host[0],port])
	s.listen(1)
	while arest.flag:
                print('lisetning')
                time.sleep(0.2)
		c,addr = s.accept() #wait client connecting...
		request_handle = c.recv(1024)#receive request 
		try: 
			arest.handle(c,request_handle)
		except (ValueError,OSError):	
			machine.reset()
		c.close() 	

	