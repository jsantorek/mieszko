import RPi.GPIO as GPIO
import time
import driver.pololu_minIMU as imu
import numpy as np

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT, initial=GPIO.HIGH)

time.sleep(1)
GPIO.output(25, GPIO.LOW)

time.sleep(1)
GPIO.output(25, GPIO.HIGH)

time.sleep(1)
GPIO.output(25, GPIO.LOW)

GPIO.cleanup()

imu.init()
clb = []
for i in range(100):
    v = imu.read_acc()
    v.extend(imu.read_gyr())
    v.extend(imu.read_mag())
    clb.append(v)
    time.sleep(0.05)
clb = np.mean(np.array(clb), axis=0)

for i in range(100):
    v = imu.read_acc()
    v.extend(imu.read_gyr())
    v.extend(imu.read_mag())
    v -= clb
    print(v)
    time.sleep(0.3)
