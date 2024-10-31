from machine import I2C, Pin
from mpu9250 import MPU9250

def do():
    print("MPU9250 example")
    # Initialize I2C
    i2c = I2C(0, scl=Pin(22), sda=Pin(21))

    # Initialize MPU9250
    mpu = MPU9250(i2c)

    # Read data from MPU9250
    print("MPU9250 id: " + hex(mpu.whoami))
    while True:
        print("tick")
        print("tick")
        print("tick")
        # print("Acceleration:", mpu.acceleration)
        # print("Gyro:", mpu.gyro)
        # print("Magnet:", mpu.magnetic)
        # print("Temperature:", mpu.temperature)
        time.sleep(1)
