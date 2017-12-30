import drivers.pololu_driver as drv
import drivers.pololu_sharp as shp
import numpy as np
import time


def motor_test():
    print("Motor tests start")

    print("Both slow forward 3 seconds")
    drv.motors.set_speeds(10, 10)
    time.sleep(3)

    print("Both fast forward 1 second")
    drv.motors.set_speeds(100, 100)
    time.sleep(1)

    print("Both slow backward 3 seconds")
    drv.motors.set_speeds(-10, -10)
    time.sleep(3)

    print("Both fast backward 1 seconds")
    drv.motors.set_speeds(-100, -100)
    time.sleep(1)

    print("Both stop 3 seconds")
    drv.motors.set_speeds(0, 0)
    time.sleep(3)

    print("Motor1 forward, Motor2 backward 2 seconds")
    drv.motors.set_speeds(10, -10)
    time.sleep(2)

    print("Motor1 backward, Motor2 forward 2 seconds")
    drv.motors.set_speeds(-10, 10)
    time.sleep(2)

    print("Motor1 stop")
    drv.motors.motor1.set_speed(0)
    time.sleep(1)

    print("Motor2 stop")
    drv.motors.motor2.set_speed(0)
    time.sleep(1)

    print("Motor tests finished")


def sharp_test():
    print("Sharp tests start")

    v = []
    print("Reading Whisker1 for 1 second")
    for i in range(10):
        v.append(shp.whiskers.whisker1.read())
        time.sleep(0.1)
    print("Whisker1 reading: {}".format(np.mean(np.ndarray(v))))

    v = []
    print("Reading Whisker2 for 1 second")
    for i in range(10):
        v.append(shp.whiskers.whisker2.read())
        time.sleep(0.1)
    print("Whisker2 reading: {}".format(np.mean(np.ndarray(v))))

    v = []
    print("Reading Whisker3 for 1 second")
    for i in range(10):
        v.append(shp.whiskers.whisker3.read())
        time.sleep(0.1)
    print("Whisker3 reading: {}".format(np.mean(np.ndarray(v))))

    v = []
    print("Reading Whisker4 for 1 second")
    for i in range(10):
        v.append(shp.whiskers.whisker4.read())
        time.sleep(0.1)
    print("Whisker4 reading: {}".format(np.mean(np.array(v))))

    v = []
    print("Reading Whisker5 for 1 second")
    for i in range(10):
        v.append(shp.whiskers.whisker5.read())
        time.sleep(0.1)
    print("Whisker5 reading: {}".format(np.mean(np.array(v))))

    v = []
    print("Reading all whiskers for 1 second")
    for i in range(10):
        v.append(shp.whiskers.read())
        time.sleep(0.1)
    print("Whisker1 reading: " + str(np.mean(np.array(v), axis=1).tolist()))

    print("Sharp tests finished")
