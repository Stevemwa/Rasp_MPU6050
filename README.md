# Rasp_gsm
Use of a  IMU module to get acceleration and gyroscopic data.

to use :

1) on your terminal type
   ```
   sudo raspi-config
   ```
   
3) select 3: ```Interface Options```
   
4) select``` I5: I2C Enable``` and Enable I2c in not enabled
   
5) get back to your terminal

   
6) on your terminal type to check addresses of connected devices
```
i2cdetect -y 1
```

    
7) on your terminal type  to install smbu2 library that will use for I2C interface
```
 pip install smbus2
```


9) cd ``` /path/to/your/desired/directory```


10) clone the repository
```     
git clone https://github.com/Stevemwa/Rasp_MPU6050.git
```

9) create your main file i.e ```main.py```


   
10) Add the script below:
   
```python
from MPU6050 import IMU
import time

if __name__ == "__main__":
mpu = IMU()

    while True:
            acceleration=mpu.get_acceleration()
            gyro=mpu.get_gyro()
            all_data=mpu.get_all_data()
            print(str(acceleration))
            print(str(gyro))
            print(str(all_data))
            time.sleep(0.5)
   
    
```
