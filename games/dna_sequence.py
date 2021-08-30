import random


def evolve(x):
    index = random.randint(0, len(x) - 1)
    p = random.randint(1, 20)
    print(p)
    if p == 1:
        if x[index] == '0':
            x[index] = '1'
        else:
            x[index] = '0'


with open('dna_data.txt') as f:
    x = f.read()
    x = list(x)

for i in range(0, 1000):
    evolve(x)
print(x)
