from machine import Pin,I2C
import time
class PCA9586():
    
    def __init__(self,addr):
        self.pin = [16,5,4,0,2,14,12,13,15,3,1,9,10] #GPIO->pin
        self.i2c = I2C(scl=Pin(self.pin[6]),sda=Pin(self.pin[7]),freq=400000)
        self.addr = addr #rgb address 
    def write_reg(self,chan_addr,command):
        self.i2c.start()
        self.i2c.writeto_mem(self.addr,chan_addr,command)
        time.sleep_ms(20)
        self.i2c.stop()
       
    def chan_reg(self,chan,reg):#choose channel
        return 0x06+chan*4+reg
    
    def set_chan_on(self,chan,on):
        value = bytearray(1)
        value[0] = 0x10*on
        self.write_reg(self.chan_reg(chan,1),value)
       
    def set_chan_off(self,chan,off):
        value = bytearray(1)
        value[0] = 0x10*off
        self.write_reg(self.chan_reg(chan,3),value)
                      
    def init(self):
        value = bytearray(1)
        value[0] = 1&0xff|0x21
        self.write_reg(0,value)
        value[0] = 1>>8&0xff|0x04
        self.write_reg(1,value)
       
    def set_chan_pwm(self,chan,val):
        if 0<val<7:
            val = 7
        val = int(4095*val/100)
        value = bytearray(4)
        value[0] = 0^0xff
        value[1] = 0>>8
        value[2] = val^0xff
        value[3] = val>>8
        self.write_reg(self.chan_reg(chan,0),value)
    

 
 
