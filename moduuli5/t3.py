numero = int(input('Anna kokonaisluku: '))
bAlkuluku = True

for i in range(2, numero):
    if numero % i == 0:
        bAlkuluku = False

if bAlkuluku and numero > 1:
    print(f'Luku {numero} on alkuluku.')
else:
    print(f'Luku {numero} ei ole alkuluku.')

