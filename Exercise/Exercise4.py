#-----------Set D1 intensity depends on the value from A0-----------

#Library
from machine import ADC,Pin,PWM
import time

#Initialiation
D = [16,5,4,0,2,14,12,13,15,3,1,9,10] #GPIO->PIN
D0 = Pin(D[0],Pin.OUT) #Set D0 as output
D1 = PWM(Pin(D[1]),freq=50,duty=0) #Set D1 as PWM

#Program1 - read A0
while 1:
	D0.value(1) 
	A0 = ADC(0).read()
	print(A0)
	D1.duty(A0)  
	time.sleep(0.2)