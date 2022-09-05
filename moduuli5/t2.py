numerot = []
numero = input('Anna numero: ')

while numero:
    numerot.append(float(numero))
    numero = input('Anna numero: ')

numerot.sort(reverse=True)
print(numerot[0:5])