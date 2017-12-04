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
for i in range(1000):
    print(imu.read_acc())

