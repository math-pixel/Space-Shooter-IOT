from machine import Pin, I2C
from mpu6050 import MPU6050

class Gyro_Sensor():

    def __init__(self, sclPin=22, sdaPin=21) -> None:
        # Setup I2C
        self.i2c = I2C(scl=Pin(sclPin), sda=Pin(sdaPin))
        # Initialize MPU6050
        self.mpu = MPU6050(self.i2c)
        # Test MPU6050 connection
        print("Testing MPU6050 connection...")
        print("MPU6050 connection successful" if self.mpu.whoami() == 0x68 else "MPU6050 connection failed")

    def getGyroData(self):
        gyro_data = self.mpu.get_gyro_data()
        return gyro_data
    
    def getAccelData(self):
        accel_data = self.mpu.get_accel_data() 
        return accel_data
    
# Read and print sensor data
# while True:
#     accel_data = mpu.get_accel_data()
#     gyro_data = mpu.get_gyro_data()
#     print("Accel: {}, {}, {}".format(accel_data['x'], accel_data['y'], accel_data['z']))
#     print("Gyro: {}, {}, {}".format(gyro_data['x'], gyro_data['y'], gyro_data['z']))
#     time.sleep(1)