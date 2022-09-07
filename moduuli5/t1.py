from random import randint

n = int(input('Anna arpakuutioiden määrä: '))
summa = 0

for i in range(n):
    summa += randint(1, 6)

print(f'Arpakuutioiden heittojen summa: {summa}')