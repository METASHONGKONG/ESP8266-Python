import machine
import pca9685

pin = [16,5,4,0,2,14,12,13,15,3,1,9,10] #GPIO->PIN
dis_i2c = machine.I2C(sda=machine.Pin(pin[7]), scl=machine.Pin(pin[6]))

pca = pca9685.PCA9685(dis_i2c)
pca.freq(60)
pca.duty(0,4095) # Set pin 0 to 0-4095