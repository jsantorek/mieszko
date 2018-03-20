import RPi.GPIO as GPIO
import time
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.cluster import KMeans
import drivers.pololu_sharp as shp
import drivers.pololu_driver as drv
import numpy as np

train_vectors = []
train_labels = []
cls1 = None
cls2 = None


def load_sets(name):
    global train_vectors
    global train_labels
    with open('training/' + name + '/lab.txt', 'r') as lab:
        for line in lab:
            train_labels.append([float(i) for i in line.split(',')])
        train_labels = np.array(train_labels)
    with open('training/' + name + '/vec.txt', 'r') as vec:
        for line in vec:
            train_vectors.append([float(i) for i in line.split(',')])
        train_vectors = np.array(train_vectors)


def load_classifiers(mode):
    global cls1
    global cls2
    if mode == 'knn':
        cls1 = KNeighborsRegressor()
        cls2 = KNeighborsRegressor()
    if mode == 'som':
        cls1 = KMeans()
        cls2 = KMeans()
    if mode == 'ann':
        cls1 = MLPRegressor(solver='lbfgs')
        cls2 = MLPRegressor(solver='lbfgs')
    cls1.fit(train_vectors, train_labels[:, 0])
    cls2.fit(train_vectors, train_labels[:, 1])


def diagnose_classifiers():
    global cls1
    global cls2
    with open('diagnostics.txt', 'w') as of:
        of.write('Classifier 1 diagnostics:\n')
        i = np.identity(5)
        o = np.ones_like(i)
        for x in range(0, 101):
            x /= 100
            xm = o - i * x
            of.write('{}\t{}\t{}\t{}\t{}\t{}\n'
                     .format(x, cls1.predict(xm[:, 0].reshape(1, -1))[0], cls1.predict(xm[:, 1].reshape(1, -1))[0],
                             cls1.predict(xm[:, 2].reshape(1, -1))[0], cls1.predict(xm[:, 3].reshape(1, -1))[0],
                             cls1.predict(xm[:, 4].reshape(1, -1))[0]))
        of.write('\nClassifier 2 diagnostics:\n')
        for x in range(0, 101):
            x /= 100
            xm = o - i * x
            of.write('{}\t{}\t{}\t{}\t{}\t{}\n'
                     .format(x,
                             cls2.predict(xm[:, 0].reshape(1, -1))[0],
                             cls2.predict(xm[:, 1].reshape(1, -1))[0],
                             cls2.predict(xm[:, 2].reshape(1, -1))[0],
                             cls2.predict(xm[:, 3].reshape(1, -1))[0],
                             cls2.predict(xm[:, 4].reshape(1, -1))[0]))


def test_classifiers():
    test_vectors = [
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1]
    ]
    for v in test_vectors:
        print('{} => [{}, {}]'.format(str(v),
                                      str(cls1.predict(np.array(v).reshape(1, -1))[0]),
                                      str(cls2.predict(np.array(v).reshape(1, -1))[0])))


def start(t=30):
    t0 = time.time()
    drv.motors.enable()
    while time.time() - t0 < t:
        v = shp.whiskers.read()
        v1 = cls1.predict(np.array(v).reshape(1, -1))[0]
        v2 = cls2.predict(np.array(v).reshape(1, -1))[0]
        print('{} => [{}, {}]'.format(str(v), str(v1), str(v2)))
        drv.motors.set_speeds(100 * v1, 100 * v2)
    drv.motors.disable()
    GPIO.cleanup()


def p1():
    load_sets('follow')
    load_classifiers('knn')
    t0 = time.time()
    time.sleep(3)
    drv.motors.enable()
    while time.time() - t0 < 30:
        v = shp.whiskers.read()
        v1 = cls1.predict(np.array(v).reshape(1, -1))[0]
        v2 = cls2.predict(np.array(v).reshape(1, -1))[0]
        print('{} => [{}, {}]'.format(str(v), str(v1), str(v2)))
        drv.motors.set_speeds(80 * v2, 80 * v1)
    drv.motors.disable()
    GPIO.cleanup()
    exit(0)


def p2():
    load_sets('avoid')
    load_classifiers('knn')
    t0 = time.time()
    drv.motors.enable()
    while time.time() - t0 < 30:
        v = shp.whiskers.read()
        v1 = cls1.predict(np.array(v).reshape(1, -1))[0]
        v2 = cls2.predict(np.array(v).reshape(1, -1))[0]
        print('{} => [{}, {}]'.format(str(v), str(v1), str(v2)))
        drv.motors.set_speeds(80 * v1, 80 * v2)
    drv.motors.disable()
    GPIO.cleanup()
    exit(0)
