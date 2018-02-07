# import RPi.GPIO as GPIO
# import time
# import drivers.pololu_imu as imu
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPClassifier
from sklearn.cluster import KMeans
import numpy as np

train_vectors = []
train_labels = []
test_vectors = [[1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
classifier = None


def load_set(name):
    global train_vectors
    global train_labels
    with open('training/' + name + '/lab.txt', 'r') as lab:
        for line in lab:
            train_labels.append([float(i) for i in line.split(',')])
    with open('training/' + name + '/vec.txt', 'r') as vec:
        for line in vec:
            train_vectors.append([float(i) for i in line.split(',')])


def load_classifier(mode):
    global classifier
    if mode == 'knn':
        classifier = KNeighborsRegressor()
    if mode == 'som':
        classifier = KMeans()
    if mode == 'ann':
        classifier = MLPClassifixer(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    classifier.fit(train_vectors, train_labels)


load_set('rand_dist')
load_classifier('knn')
for v in test_vectors:
    print('{} => {}'.format(str(v), str(classifier.predict(np.array(v).reshape(1, -1)))))

'''
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

# GPIO.cleanup()
