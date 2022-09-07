from random import randint
tahkot = int(input('Nopan tahkojen määrä: '))

def nopanheitot(n):
    return randint(1, n)

heitto = 0
while heitto != tahkot:
    heitto = nopanheitot(tahkot)
    print(heitto)
