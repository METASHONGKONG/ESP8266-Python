from machine import ADC,PWM
import json
from si7021 import *
from pca9586 import *
from pm import *
class aREST:
	flag = 1
	def handle(self,client,request_handle):
		pin = [16,5,4,0,2,14,12,13,15,3,1,9,10] #GPIO->pin
		mode = ''
		num = ''
		value = ''
		g = ''
		b = ''
		w = ''
		answer={}
		pin5 = Pin(pin[5],Pin.OUT)
		pin3 = Pin(pin[3],Pin.OUT)
		req = request_handle.decode('UTF-8','strict')
		c = client
		#find start
		e = req.find('/')
		req = req[e+1:]
		#find end
		e = req.find('HTTP')
		req = req[:e-1]
		#find mode
		e = req.find('/')
		if -1 == e:
			mode = req
		else:
			mode = req[:e]
			#find pin num
			req = req[e+1:]
			e = req.find('/')
			if -1 == e:
				num = req
			else:
				num = req[:e]
				#find value
				req = req[e+1:]
				e = req.find('/')
				if -1 == e:
					value = req
				else:
					value = req[:e]
					#find green led
					req = req[e+1:]
					e = req.find('/')
					if -1 == e:
						g = req
					else:
						g = req[:e]
						#find blue led
						req = req[e+1:]
						e = req.find('/')
						if -1 == e:
							b = req
						else:
							b = req[:e]
							#find white led
							w = req[e+1:] 
					
		if mode == 'exit':
			self.flag = 0
			answer['message'] = 'A socket to stop working,start again please restart'
		if mode == 'mode':
			if value == 'o':
				answer['message'] = 'Pin '+num+' set to output'
			if value == 'i':
				answer['message'] = 'Pin '+num+' set to input'
		if mode == 'digital':
			if value == '0':
				pin_out = Pin(pin[int(num)],Pin.OUT)
				pin_out.value(0)
				answer['message'] = 'Pin '+num+' set to 0'
			if value == '1':
				pin_out = Pin(pin[int(num)],Pin.OUT)
				pin_out.value(1)
				answer['message'] = 'Pin '+num+' set to 1'
			if value == 'r':
				pin_in = Pin(pin[int(num)],Pin.IN)
				read_value = pin_in.value()
				answer['message'] = 'Pin '+num+' read value '+str(read_value)
		if mode == 'analog':
			if num == '0':
				pin_out = Pin(pin[8],Pin.OUT)
				pin_out.value(1)
			if num == '1':
				pin_out = Pin(pin[8],Pin.OUT)
				pin_out.value(0)	
			adc_value = ADC(0).read()
			answer['message'] = 'A'+num+' value:'+str(adc_value)
		if mode == 'pwm':
			pin_pwm = PWM(Pin(pin[int(num)]),freq=100,duty=int(value))#pwm init
			answer['message'] = 'PWM:Pin '+num+' set to '+value
		if mode == 'temperature':
			self.si7021 = SI7021()
			answer['message'] = "Temperature('C):"+str(self.si7021.temp_value())
		if mode == 'humidity':
			self.si7021 = SI7021()
			answer['message'] = 'Humidity(%RH):'+str(self.si7021.humi_value())	
		if mode == 'forward':
			pin5.value(1)
			pin3.value(1)
			answer['message'] = 'car forward now...'
		if mode == 'rgb':
			self.pca9586 = PCA9586(int(num))
			self.pca9586.init()
			if value == 'off':
				self.pca9586.set_chan_off(0,1)#red led
				self.pca9586.set_chan_off(1,1)#green led
				self.pca9586.set_chan_off(2,1)#blue led
				self.pca9586.set_chan_off(3,1)#white led
				answer['message'] = 'RGB off'
			else:
				self.pca9586.set_chan_pwm(0,int(value))#red led
				self.pca9586.set_chan_pwm(1,int(g))#green led
				self.pca9586.set_chan_pwm(2,int(b))#blue led
				self.pca9586.set_chan_pwm(3,int(w))#white led
				answer['message'] = 'set RGB ok'
		if mode == 'pm':
			#self.pm = PM()
			value = PM().pm_value()
			answer['message'] = 'PM2.5 value: '+str(value)
		#send answer	
		c.send('HTTP/1.1 200 OK\r\nContent-type: text/html\r\nAccess-Control-Allow-Origin:* \r\n\r\n'+json.dumps(answer)+'\r\n')	
		
		
