import RPi.GPIO as GPIO
import time
import driver.pololu_minIMU as imu

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
tmp = []
for i in range(100):
    tmp.append([imu.read_acc(), imu.read_gyr(), imu.read_mag()])
    time.sleep(0.05)
clb = [0, 0, 0]
for t in tmp:
    clb[0] += t[0]
    clb[1] += t[1]
    clb[2] += t[2]

for c in clb:
    clb /= 100

for i in range(100):
    a = imu.read_acc()
    b = imu.read_gyr()
    c = imu.read_mag()
    a[0] -= clb[0][0]
    a[1] -= clb[0][1]
    a[2] -= clb[0][2]
    b[0] -= clb[1][0]
    b[1] -= clb[1][1]
    b[2] -= clb[1][2]
    c[0] -= clb[2][0]
    c[1] -= clb[2][1]
    c[2] -= clb[2][2]
    print("[] => {} : {} : {}".format(i, a, b, c))
    time.sleep(0.3)
