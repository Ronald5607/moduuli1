from random import uniform

N = int(input('Anna pisteiden kokonaismäärä: '))
n = 0
i = 0

while i < N:
    x = uniform(-1, 1)
    y = uniform(-1, 1)
    if x**2 + y**2 < 1:
        n += 1
    i += 1

print(f'piin likiarvo on {4*n/N}')