#-----------Set D4 servo degree 180 > 90 > 0 > 90 > 180-----------

#Import library
from machine import Pin,PWM 
import math
import time

#Servo function
def degree(duty):
	return math.floor(33+((128-33)*duty)/180);
	
#Initialization
D = [16,5,4,0,2,14,12,13,15,3,1,9,10] 
D4 = PWM(Pin(D[4]),freq=50,duty=0) #Set D4 as PWM

#Program
D4.duty(degree(180))
time.sleep(1)
D4.duty(degree(90)) 
time.sleep(1)
D4.duty(degree(0))  
time.sleep(1)
D4.duty(degree(90)) 
time.sleep(1)
D4.duty(degree(180))
time.sleep(1)	