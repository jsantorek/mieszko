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
clb = np.array([9, 0])
for i in range(100):
    v = imu.read_acc().extend(imu.read_gyr().extend(imu.read_mag()))
    np.append(clb, v, axis=0)
    time.sleep(0.05)
clb = np.mean(clb, axis=0)

for i in range(100):
    v = imu.read_acc().extend(imu.read_gyr().extend(imu.read_mag()))
    v -= clb
    print("[] => {}".format(i, v))
    time.sleep(0.3)
