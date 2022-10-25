from moduuli9.t123 import Auto
from random import randint
from moduuli9.t4 import tee_autot


class Kilpailu:

    def __init__(self, nimi: str, matka_kilometreina: int, autolista: list[Auto]):
        self.nimi = nimi
        self.matka = matka_kilometreina
        self.autot = autolista

    def tunti_kuluu(self) -> None:
        for auto in self.autot:
            auto.kiihdyta(randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self) -> None:
        rekisteri = 'rekisterinumero:'
        huippu = 'huippunopeus:'
        nopeus = 'nopeus:'
        matka = 'matka:'
        print(rekisteri, huippu, nopeus, matka)
        for auto in self.autot:
            print(str(auto.rekisteritunnus) + (len(rekisteri) - len(str(auto.rekisteritunnus))) * ' ',
                  str(auto.huippunopeus) + (len(huippu) - len(str(auto.huippunopeus))) * ' ',
                  str(auto.nopeus) + (len(nopeus) - len(str(auto.nopeus))) * ' ',
                  str(auto.matka) + (len(matka) - len(str(auto.matka))) * ' '
                  )

    def kilpailu_ohi(self) -> bool:
        for auto in self.autot:
            if auto.matka > self.matka:
                return True
        return False


if __name__ == '__main__':
    kilpailu = Kilpailu('Suuri romuralli', 8000, tee_autot(10))

    tunti = 0
    while not kilpailu.kilpailu_ohi():
        print('tunti:', tunti)
        kilpailu.tulosta_tilanne()
        for _ in range(10):
            kilpailu.tunti_kuluu()
            tunti += 1
            if kilpailu.kilpailu_ohi():
                break

    print('Kilpailu loppu. Kesto oli', tunti, 'tuntia.')
    kilpailu.tulosta_tilanne()