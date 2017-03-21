#-----------Read input value-----------

#Inialization
from machine import ADC
from machine import Pin
D = [16,5,4,0,2,14,12,13,15,3,1,9,10] #GPIO->PIN
D0 = Pin(D[0],Pin.OUT) #Set D0 as output

#Program1 - read A0
D0.value(1) #0:LOW,1:HIGH
A0 = ADC(0).read()
print(A0)

#Program2 - read A1
D0.value(0) #0:LOW,1:HIGH
A1 = ADC(0).read()
print(A1)