tuuma = 5

while tuuma > 0:
    tuuma = float(input('Monta tuumaa? '))
    if tuuma > 0:
        print(f'{tuuma} tuumaa on {tuuma*2.54} cm.')

print('Ei negatiivisia arvoja.')