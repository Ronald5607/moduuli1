nimet = set()
nimi = input('Anna nimi: ')

while nimi:
    if nimi in nimet:
        print('Aiemmin syötetty nimi.')
    else:
        nimet.add(nimi)
        print('Uusi nimi')
    nimi = input('Anna nimi: ')

for i in nimet:
    print(i)
