#-----------Set servo D4 to 180 degree-----------

#Import library
from machine import Pin,PWM 
import math

#Servo function
def degree(duty):
	return math.floor(33+((128-33)*duty)/180);
	
#Program
D = [16,5,4,0,2,14,12,13,15,3,1,9,10] #Initialization(GPIO->METAS PIN)
D4 = PWM(Pin(D[4]),freq=50,duty=0) #Set D4 as PWM
D4.duty(degree(180))  #Set servo to 180 degree