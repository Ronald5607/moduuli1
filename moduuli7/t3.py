jatka = True
lentokentat = {}

while jatka:
    komento = input('Syötä komento (lisää/tieto/lopeta): ')
    if komento == 'lisää':
        ICAO = input('Anna ICAO tunnus: ')
        nimi = input('Anna lentokentän nimi: ')
        lentokentat[ICAO] = nimi
    elif komento == 'tieto':
        icao = input('Anna ICAO tunnus: ')
        print(lentokentat[icao])
    elif komento == 'lopeta':
        jatka = False
    else:
        print('Komentoa ei tunnistettu.')