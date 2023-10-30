# Rasp_gsm
Use of a  IMU module to get acceleration and gyroscopic dats.

to use :

1) on your terminal type ``` sudo raspi-config```
   
2) select 3: Interface Options
   
3) select I5: I2C Enable and Enable I2c in not enabled
   
4) get back to your terminal

   
5) on your terminal type ``` i2cdetect -y 1``` to check addresses of connected devices

    
6) on your terminal type ``` pip install smbus2``` library that will use for I2C interface

7) cd ``` /path/to/your/desired/directory```


8) clone the repository
```     
git clone https://github.com/Stevemwa/Rasp_gsm/blob/906c9a2102cefd5390ee31cd6d628c2672a2e3c4/gsm.py
```

9) create your main file i.e ```main.py```


   
10) Add the script below:
   
```python
from MPU6050 import IMU
import time

if __name__ == "__main__":
mpu = IMU()

    while True:
            accel_data, gyro_data = mpu.read_data()
            print("Accelerometer Data (g):", accel_data)
            print("Gyroscope Data (degrees/s):", gyro_data)
            time.sleep(1)
   
    
```
