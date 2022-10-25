class Julkaisu:
    def __init__(self, nimi: str):
        self.nimi = nimi

    def tulosta_tiedot(self):
        for key, value in self.__dict__.items():
            print(f'{key}: {value}')


class Kirja(Julkaisu):
    def __init__(self, nimi: str, kirjoittaja: str, sivumäärä: int):
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä


class Lehti(Julkaisu):
    def __init__(self, nimi: str, päätoimittaja: str, sivumäärä: int):
        self.nimi = nimi
        self.päätoimittaja = päätoimittaja
        self.sivumäärä = sivumäärä


k = Kirja('aa', 'bb', 200)
k.tulosta_tiedot()
l = Lehti('cc', 'dd', 150)
l.tulosta_tiedot()
