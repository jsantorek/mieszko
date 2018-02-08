import random
import csv

v_dir = -1
v_in = []
v_out = []

print('\nnothing - forward')
for h in range(5):
    v = [random.randrange(9, 11) / 10 for _ in range(5)]
    print(v)
    v_in.append(v)
    v_out.append([v_dir, v_dir])

print('\nrandom distribution - stop')
for i in range(5):
    v = [random.randrange(0, 11) / 10 for _ in range(5)]
    print(v)
    v_in.append(v)
    v_out.append([0, 0])

print('\nnothing or small noise - forward')
for j in range(50):
    v = [random.randrange(7, 11) / 10 for _ in range(random.randrange(0, 3))]
    while len(v) < 5:
        v.append(1)
    random.shuffle(v)
    print(v)
    v_in.append(v)
    v_out.append([v_dir, v_dir])

print('\nsignal registered in front - stop')
for k in range(30):
    v = [random.randrange(7, 11) / 10,
         random.randrange(0, 11) / 10,
         random.randrange(0, 3) / 10,
         random.randrange(0, 11) / 10,
         random.randrange(7, 11) / 10]
    print(v)
    v_in.append(v)
    v_out.append([0, 0])

print('\nsignal registered on side - stop')
for l in range(30):
    v = [random.randrange(0, 2) / 10,
         random.randrange(0, 7) / 10,
         random.randrange(4, 11) / 10,
         random.randrange(7, 11) / 10,
         1]
    print(v)
    v_in.append(v)
    v_out.append([0, 0])

for m in range(30):
    v = [1,
         random.randrange(7, 11) / 10,
         random.randrange(4, 11) / 10,
         random.randrange(0, 7) / 10,
         random.randrange(0, 2) / 10]
    print(v)
    v_in.append(v)
    v_out.append([0, 0])

with open('../training/stop/vec.txt', 'w', newline='') as vec:
    writer = csv.writer(vec, delimiter=',')
    for v in v_in:
        writer.writerow(v)

with open('../training/stop/lab.txt', 'w', newline='') as lab:
    writer = csv.writer(lab, delimiter=',')
    for v in v_out:
        writer.writerow(v)
