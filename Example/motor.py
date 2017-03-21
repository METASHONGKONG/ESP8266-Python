#-----------Motor operation-----------

from machine import Pin,PWM #Import library

#Initialization
D = [16,5,4,0,2,14,12,13,15,3,1,9,10] #Initialization(GPIO->METAS PIN)
M1_CW = PWM(Pin(D[2]),freq=50,duty=0) #Set D2 as PWM
M1_ACW = PWM(Pin(D[3]),freq=50,duty=0) #Set D3 as PWM 
M2_CW = PWM(Pin(D[5]),freq=50,duty=0) #Set D5 as PWM 
M2_ACW = PWM(Pin(D[4]),freq=50,duty=0) #Set D4 as PWM 

#----------- Motor 1 -----------

#Turn motor 1 clockwise in 500
M1_CW.duty(500)  
M1_ACW.duty(0)

#Turn motor 1 anticlockwise in 1023
M1_CW.duty(1023)  
M1_ACW.duty(0)

#Stop motor 1
M1_CW.duty(0)  
M1_ACW.duty(0)

#----------- Motor 2 -----------

#Turn motor 2 clockwise in 1023
M2_CW.duty(1023)  
M2_ACW.duty(0)

#Turn motor 2 anticlockwise in 1023
M2_CW.duty(0  
M2_ACW.duty(1023)

#Stop motor 2
M2_CW.duty(0)  
M2_ACW.duty(0)