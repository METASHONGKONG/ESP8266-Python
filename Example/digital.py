#-----------Set D1 to High-----------

from machine import Pin #Import library

D = [16,5,4,0,2,14,12,13,15,3,1,9,10] #Initialization(GPIO->METAS PIN)
D1 = Pin(D[1],Pin.OUT) #Set D1 as output
D1.value(1) #0:LOW,1:HIGH