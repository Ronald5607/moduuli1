class Julkaisu:
    def __init__(self, nimi: str):
        self.nimi = nimi

    # def tulosta_tiedot(self):
    #     for key, value in self.__dict__.items():
    #         print(f'{key}: {value}')


class Kirja(Julkaisu):
    def __init__(self, nimi: str, kirjoittaja: str, sivumäärä: int):
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self) -> None:
        print(self.nimi, self.kirjoittaja, self.sivumäärä, sep=', ')


class Lehti(Julkaisu):
    def __init__(self, nimi: str, päätoimittaja: str):
        self.nimi = nimi
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self) -> None:
        print(self.nimi, self.päätoimittaja, sep=', ')


"""Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua)"""
k = Kirja('Hytti n:o 6', 'Rosa Liksom', 200)
k.tulosta_tiedot()
l = Lehti('Aku Ankka', 'Aki Hyyppä')
l.tulosta_tiedot()
