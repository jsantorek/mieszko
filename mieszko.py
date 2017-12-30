import RPi.GPIO as GPIO
import time
import drivers.pololu_imu as imu
import numpy as np

#'''
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)


imu.init()
clb = []
for i in range(50):
    v = imu.read_acc()
    v.extend(imu.read_gyr())
    v.extend(imu.read_mag())
    clb.append(v)
    time.sleep(0.1)
print('Calibration')
print(np.std(np.array(clb), axis=0))
print(np.mean(np.array(clb), axis=0))
clb = np.mean(np.array(clb), axis=0)
for i in range(100):
    V = []
    for j in range(5):
        v = imu.read_acc()
        v.extend(imu.read_gyr())
        v.extend(imu.read_mag())
        time.sleep(0.1)
        V.append(v)
    V = np.mean(np.array(V), axis=0) - clb
    V = V.astype(np.int16)
    print(V)
#'''

GPIO.cleanup()
