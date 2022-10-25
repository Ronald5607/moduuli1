from moduuli9.t123 import Auto
from random import randint


def tee_autot(maara: int) -> list[Auto]:
    return [Auto(f'ABC-{n+1}', randint(100, 200)) for n in range(maara)]


def aja_kisa(autolista: [Auto], pituus: int) -> None:
    max_matka = 0
    while max_matka < pituus:
        for auto in autolista:
            auto.kiihdyta(randint(-10, 15))
            auto.kulje(1)
            if auto.matka > max_matka:
                max_matka = auto.matka


if __name__ == '__main__':
    autot = tee_autot(10)
    aja_kisa(autot, 10000)
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