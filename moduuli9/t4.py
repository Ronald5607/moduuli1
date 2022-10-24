from t123 import Auto
from random import randint

autot = [Auto(f'ABC-{n+1}', randint(100, 200)) for n in range(10)]

max_matka = 0
while max_matka < 10000:
    for auto in autot:
        auto.kiihdyta(randint(-10, 15))
        auto.kulje(1)
        if auto.matka > max_matka:
            max_matka = auto.matka


rekisteri = 'rekisterinumero:'
huippu = 'huippunopeus:'
nopeus = 'nopeus:'
matka = 'matka:'
print(rekisteri, huippu, nopeus, matka)
for auto in autot:
    print(str(auto.rekisteritunnus) + (len(rekisteri)-len(str(auto.rekisteritunnus)))*' ',
          str(auto.huippunopeus) + (len(huippu)-len(str(auto.huippunopeus)))*' ',
          str(auto.nopeus) + (len(nopeus)-len(str(auto.nopeus)))*' ',
          str(auto.matka) + (len(matka)-len(str(auto.matka)))*' '
          )