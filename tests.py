import drivers.pololu_driver as drv
import drivers.pololu_sharp as shp
import drivers.pololu_imu as imu
import numpy as np
import time


def motor_test():
    print("Motor tests started")
    drv.motors.enable()
    time.sleep(3)

    print("Both slow forward 5 seconds")
    drv.motors.set_speeds(50, 50)
    time.sleep(5)

    print("Both fast forward 5 seconds")
    drv.motors.set_speeds(100, 100)
    time.sleep(5)

    print("Both slow backward 5 seconds")
    drv.motors.set_speeds(-50, -50)
    time.sleep(5)

    print("Both fast backward 5 seconds")
    drv.motors.set_speeds(-100, -100)
    time.sleep(5)

    print("Both stop 3 seconds")
    drv.motors.set_speeds(0, 0)
    time.sleep(3)

    print("Motor1 forward, Motor2 backward 5 seconds")
    drv.motors.set_speeds(50, -50)
    time.sleep(5)

    print("Motor1 backward, Motor2 forward 5 seconds")
    drv.motors.set_speeds(-50, 50)
    time.sleep(5)

    print("Motor1 stop")
    drv.motors.motor1.set_speed(0)
    time.sleep(1)

    print("Motor2 stop")
    drv.motors.motor2.set_speed(0)
    time.sleep(1)

    print("Motor tests finished")
    drv.motors.disable()


def sharp_test():
    print("Sharp tests started")

    v = []
    print("Reading Whisker1 for 1 second")
    for i in range(10):
        v.append(shp.whiskers.whisker1.read())
        time.sleep(0.1)
    print("Whisker1 reading: {}".format(np.mean(v)))

    v = []
    print("Reading Whisker2 for 1 second")
    for i in range(10):
        v.append(shp.whiskers.whisker2.read())
        time.sleep(0.1)
    print("Whisker2 reading: {}".format(np.mean(v)))

    v = []
    print("Reading Whisker3 for 1 second")
    for i in range(10):
        v.append(shp.whiskers.whisker3.read())
        time.sleep(0.1)
    print("Whisker3 reading: {}".format(np.mean(v)))

    v = []
    print("Reading Whisker4 for 1 second")
    for i in range(10):
        v.append(shp.whiskers.whisker4.read())
        time.sleep(0.1)
    print("Whisker4 reading: {}".format(np.mean(v)))

    v = []
    print("Reading Whisker5 for 1 second")
    for i in range(10):
        v.append(shp.whiskers.whisker5.read())
        time.sleep(0.1)
    print("Whisker5 reading: {}".format(np.mean(v)))

    v = []
    print("Reading all whiskers for 1 second")
    for i in range(10):
        v.append(shp.whiskers.read())
        time.sleep(0.1)
    print("Whisker1 reading: " + str(np.mean(v, axis=0)))

    print("Sharp tests finished")


def imu_test():
    print("Imu tests started")
    imu.init()
    try:
        print("Accelerator results")
        while True:
            time.sleep(0.2)
            print(str(imu.read_acc()))
    except KeyboardInterrupt:
        pass
    try:
        print("Gyroscope results")
        while True:
            time.sleep(0.2)
            print(str(imu.read_gyr()))
    except KeyboardInterrupt:
        pass
    try:
        print("Magnetometer results")
        while True:
            time.sleep(0.2)
            print(str(imu.read_mag()))
    except KeyboardInterrupt:
        pass
    print("Imu tests finished")
