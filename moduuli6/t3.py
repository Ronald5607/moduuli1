def muunnos(gallona):
    return 3.78541178*gallona

numero = float(input('Gallonat: '))
while numero >= 0:
    print(muunnos(numero))
    numero = float(input('Gallonat: '))
