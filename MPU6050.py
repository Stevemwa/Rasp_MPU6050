# {sudo raspi-config}:
#                     3:Interface options :
#                                         I5: I2C enable
# {i2cdetect -y 1} and :to get address of connected devices


import smbus2 
from time import sleep

class IMU:
    def __init__(self, bus=1, address=0x68):
        self.bus = smbus2.SMBus(bus)
        self.address = address

        # MPU6050 configuration
        self.bus.write_byte_data(self.address, 0x6B, 0)  # Wake up the MPU6050 (power management register)
        self.bus.write_byte_data(self.address, 0x19, 0)  # Set sample rate divider to 0 for maximum sensitivity
        self.bus.write_byte_data(self.address, 0x1A, 0x03)  # Set DLPF (Digital Low Pass Filter) to 42Hz
        self.bus.write_byte_data(self.address, 0x1B, 0x00)  # Set the gyro range to +/- 250 degrees/sec
        self.bus.write_byte_data(self.address, 0x1C, 0x00)  # Set the accelerometer range to +/- 2g

    def read_data(self):
        data = self.bus.read_i2c_block_data(self.address, 0x3B, 14)
        
        # Combine the high and low bytes to get the raw data
        accelerometer_data = [
            (data[0] << 8 | data[1]),
            (data[2] << 8 | data[3]),
            (data[4] << 8 | data[5])
        ]
        gyro_data = [
            (data[8] << 8 | data[9]),
            (data[10] << 8 | data[11]),
            (data[12] << 8 | data[13])
        ]
        
        # Convert to actual values (acceleration in g, angular velocity in degrees/s)
        acceleration = [val / 16384.0 for val in accelerometer_data]
        gyro = [val / 131.0 for val in gyro_data]
        
        return acceleration, gyro

    
    
    

   