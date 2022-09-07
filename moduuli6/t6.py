import math


def pizza(r, hinta):
    return hinta / (math.pi * (r * 0.01)**2)


s1 = float(input('Ensimmäisen pitsan säde senttimetreinä: '))
h1 = float(input('Ensimmäisen pitsan hinta euroina: '))
s2 = float(input('Toisen pitsan säde senttimetreinä: '))
h2 = float(input('Toisen pitsan hinta euroina: '))

hk1 = pizza(s1, h1)
hk2 = pizza(s2, h2)

print(f'Ensimmäisen pitsan hintakoko suhde on {hk1:.2f} €/m^2')
print(f'Toisen pitsan hintakoko suhde on {hk2:.2f} €/m^2')
if hk1 < hk2:
    print('Ensimmäinen pitsa on halvempi.')
else:
    print('Toinen pitsa on halvempi.')