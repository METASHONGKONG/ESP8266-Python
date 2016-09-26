from machine import Pin,ADC
import time
class PM():
    def __init__(self):
        self.pin = [16,5,4,0,2,14,12,13,15,3,1,9,10] #GPIO->pin
        self.pin1 = Pin(self.pin[1],Pin.OUT)
        self.pin8 = Pin(self.pin[8],Pin.OUT)
        self.pin8.value(1)
        self.adc = ADC(0)
    def pm_value(self):
        self.pin1.value(0)
        time.sleep_us(280)
        value = self.adc.read()
        time.sleep_us(40)
        self.pin1.value(1)
        time.sleep_us(9680)
        return value+270
        
        
