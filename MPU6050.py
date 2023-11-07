# {sudo raspi-config}:
#                     3:Interface options :
#                                         I5: I2C enable
# {i2cdetect -y 1} and :to get address of connected devices


import smbus2 
from time import sleep

class IMU:
    #MPU_6050 registers
    ACCEL_XOUT0 = 0x3B
    ACCEL_YOUT0 = 0x3D
    ACCEL_ZOUT0 = 0x3F
    GYRO_XOUT0 = 0x43
    GYRO_YOUT0 = 0x45
    GYRO_ZOUT0 = 0x47


    def __init__(self, bus=1, address=0x68):
        self.bus = smbus2.SMBus(bus)
        self.address = address

        # MPU6050 configuration
        self.bus.write_byte_data(self.address, 0x6B, 0)  # Wake up the MPU6050 (power management register)
        self.bus.write_byte_data(self.address, 0x19, 0)  # Set sample rate divider to 0 for maximum sensitivity
        self.bus.write_byte_data(self.address, 0x1A, 0x03)  # Set DLPF (Digital Low Pass Filter) to 42Hz
        self.bus.write_byte_data(self.address, 0x1B, 0x00)  # Set the gyro range to +/- 250 degrees/sec
        self.bus.write_byte_data(self.address, 0x1C, 0x10)  # Set the accelerometer range to +/- 8g
        self.bus.write_byte_data(self.address, 0x1B, 0x10)  # Set  Gyro range to 1000 Degrees

    def read_data(self,register):
        data_high = self.bus.read_byte_data(self.address, register)
        data_low = self.bus.read_byte_data(self.address, register + 1)
        data =(data_high << 8)+ data_low
        if (data >= 0x8000):
            return -((65535 - data) + 1)
        else:
            return data

    def get_acceleration(self):
         x = self.read_i2c_word(self.ACCEL_XOUT0)
         y = self.read_i2c_word(self.ACCEL_YOUT0)
         z = self.read_i2c_word(self.ACCEL_ZOUT0)
         x=float(x)/4096.0
         y=float(y)/4096.0
         z=float(z)/4096.0
         return x,y,z
    
    def get_gyro(self):
        x = self.read_i2c_word(self.GYRO_XOUT0)
        y = self.read_i2c_word(self.GYRO_YOUT0)
        z = self.read_i2c_word(self.GYRO_ZOUT0)
        x=float(x)/1000.0
        y=float(y)/1000.0
        z=float(z)/1000.0
        return x,y,z
    
    def get_all_data(self):
        a = self.get_accel_data()
        g = self.get_gyro_data()
        return [a,g]



        
       
    


    
    
    

   