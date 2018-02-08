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
test_vectors = [
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1]
]
cls1 = None
cls2 = None


def load_set(name):
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


def load_classifier(mode):
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


load_set('stop')
load_classifier('knn')
for v in test_vectors:
    v1 = cls1.predict(np.array(v).reshape(1, -1))[0]
    v2 = cls2.predict(np.array(v).reshape(1, -1))[0]
    print('{} => [{}, {}]'.format(str(v), str(v1), str(v2)))

t0 = time.time()
time.sleep(3)
drv.motors.enable()
while True:
    v = shp.whiskers.read()
    v1 = cls1.predict(np.array(v).reshape(1, -1))[0]
    v2 = cls2.predict(np.array(v).reshape(1, -1))[0]
    print('{} => [{}, {}]'.format(str(v), str(v1), str(v2)))
    drv.motors.set_speeds(100*v1, 100*v2)
    if time.time() - t0 > 30:
        break
    else:
        time.sleep(0.1)

GPIO.cleanup()
