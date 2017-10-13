import machine
import servo
import time

# GPIO->PIN
pin = [16,5,4,0,2,14,12,13,15,3,1,9,10] 

# Initialize I2C
dis_i2c = machine.I2C(sda=machine.Pin(pin[7]), scl=machine.Pin(pin[6]))
servos = servo.Servos(dis_i2c)

# Main program
servos.position(0, degrees=180)
time.sleep(3)
servos.position(0, degrees=0)