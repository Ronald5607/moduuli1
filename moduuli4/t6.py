from random import random

N = int(input('Anna pisteiden kokonaismäärä: '))
n = 0
i = 0

while i < N:
    x = random()
    y = random()
    if x**2 + y**2 < 1:
        n += 1
    i += 1

print(4*n/N)