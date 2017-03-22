#-----------Set D1 will be turned off after 2 second-----------

#Import library
from machine import Pin
import time

#Initialization
D = [16,5,4,0,2,14,12,13,15,3,1,9,10] 
   
#Program
D1 = Pin(D[1],Pin.OUT)
                                    
D1.value(1) 
time.sleep(2) 
D1.value(0) 
