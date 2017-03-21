#-----------Set D1 to pwm 1023-----------

from machine import Pin,PWM #Import library

D = [16,5,4,0,2,14,12,13,15,3,1,9,10] #Initialization(GPIO->METAS PIN)
D1 = PWM(Pin(D[1]),freq=50,duty=0) #Set D1 as PWM
D1.duty(1023)  #duty:0~1023
