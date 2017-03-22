#-----------Set D8 blinking every 1 second for 5 times-----------

#Import library
from machine import Pin
import time

#Initialization
D = [16,5,4,0,2,14,12,13,15,3,1,9,10] 
   
#Program
D8 = Pin(D[8],Pin.OUT)
  
for x in range(5):
	D8.value(1) 
	time.sleep(1) 
	D8.value(0) 
	time.sleep(1)