import random

v_dir = 1

v_in = []
v_out = []


def simulate(vec):
    m1 = 0
    m2 = len(vec)
    return [m1, m2]


print('\nrandom distribution - stop robot')
for i in range(20):
    v = [random.randrange(0, 11) / 10 for _ in range(5)]
    print(v)
    v_in.append(v)
    v_out.append([0, 0])

print('\nnothing or small noise - forward')
for j in range(20):
    v = [random.randrange(0, 3) / 10 for _ in range(random.randrange(0, 3))]
    while len(v) < 5:
        v.append(0)
    random.shuffle(v)
    print(v)
    v_in.append(v)
    v_out.append([v_dir, v_dir])

print('\nsignal registered in front - full backward')
for k in range(30):
    v = [random.randrange(0, 3) / 10,
         random.randrange(0, 11) / 10,
         random.randrange(2, 11) / 10,
         random.randrange(0, 11) / 10,
         random.randrange(0, 3) / 10]
    print(v)
    v_in.append(v)
    v_out.append([-v_dir, -v_dir])

print('\nsignal registered on side - turn slightly')
for l in range(30):
    v = [random.randrange(3, 11) / 10,
         random.randrange(1, 11) / 10,
         random.randrange(0, 5) / 10,
         random.randrange(0, 2) / 10,
         0]
    print(v)
    v_in.append(v)
    v_out.append([-v_dir, -0.5 * v_dir])

for m in range(30):
    v = [0,
         random.randrange(0, 2) / 10,
         random.randrange(0, 5) / 10,
         random.randrange(1, 11) / 10,
         random.randrange(3, 11) / 10]
    print(v)
    v_in.append(v)
    v_out.append([-0.5 * v_dir, v_dir])

with open('vec.txt', 'w') as vec:
    for v in v_in:
        vec.write(str(v)+'\n')

with open('lab.txt', 'w') as lab:
    for v in v_out:
        lab.write(str(v)+'\n')
