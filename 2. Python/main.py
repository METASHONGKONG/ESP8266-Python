'''
	NodeMcu(ESP8266) Dev
	Designed By Tom
	Copyright (c) 2016 METAS
'''
import network
import ssd1306
import time
from machine import Pin,I2C,ADC
import machine 
import ustruct
from aREST import *
pin = [16,5,4,0,2,14,12,13,15,3,1,9,10] #GPIO->PIN
pin5 = Pin(pin[5],Pin.OUT)# init car control:stop
pin3 = Pin(pin[3],Pin.OUT)
pin5.value(0)
pin3.value(0)
pin8 = Pin(pin[8],Pin.OUT)#adc channel choose
pin8.value(1)
adc = ADC(0).read()
  
dis_i2c = I2C(sda=Pin(pin[7]), scl=Pin(pin[6]))
display = ssd1306.SSD1306_I2C(128,32, dis_i2c, 60)
b = ustruct.unpack('BBBB',machine.unique_id())
flag_num = str(b[0]+b[1]+b[2]+b[3])
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='Metas_'+flag_num,password='12345678')     
if adc > 800:
	import os
	os.remove('wifi.py') 
	#machine.reset()
else:	
	
	try:
		import wifi
	except:
		display.fill(0)
		display.text('METAS IOT',30,8,1)
		display.text('Input  Wifi',22,25,1)
		display.show()
		time.sleep(5)
		display.fill(0)
		display.text('Metas_'+flag_num,0,0,1)
		display.text('12345678',0,10,1)
		display.text('192.168.4.1',0,20,1)
		display.show()
		import wifi_config
	#dis_i2c = I2C(sda=Pin(pin[7]), scl=Pin(pin[6]))
	#display = ssd1306.SSD1306_I2C(128,32, dis_i2c, 60)
	#from aREST import *
	import socket
	arest = aREST()#class
	wlan = network.WLAN(network.STA_IF)#station mode
	wlan.active(True)
	wlan.connect(wifi.ssid,wifi.pwd)#connect wlan
	display.fill(0)
	display.text('WIFI',0,2,1)
	display.text(wifi.ssid,0,16,1)
	display.text(wifi.pwd,0,25,1)
	display.show()
	time.sleep(5)
	while not wlan.isconnected():
		display.fill(0)
		display.text('METAS IOT',30,8,1)
		display.text('please wait',20,16,1)
		display.text('connecting...',20,24,1)
		display.show()

	print('network config:', wlan.ifconfig())#getip
	display.fill(0)
	display.text('METAS IOT',30,2,1)
	display.text(wlan.ifconfig()[0],0,25,1)
	display.show()
	s = socket.socket()#create socket
	host = wlan.ifconfig()#get hostname
	port = 80#listen port
	s.bind([host[0],port])
	s.listen(1)
	while arest.flag:
                
		c,addr = s.accept() #wait client connecting...
		request_handle = c.recv(1024)#receive request 
		try: 
			#print(request_handle)
			arest.handle(c,request_handle)
		except (ValueError,OSError):	
			machine.reset()
		c.close() 	

	