from moduuli9.t123 import Auto

"""Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto. Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena on bensatankin koko litroina. Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa. Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat."""


class Sähköauto(Auto):
    def __init__(self, rekisterinumero: str, huippunopeus: int, akkukapasiteetti: float):
        super().__init__(rekisterinumero, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def __str__(self) -> str:
        return super().__str__() + '\n' + f'Auton akkukapasiteetti on: {self.akkukapasiteetti} kwh'


class Polttomoottoriauto(Auto):
    def __init__(self, rekisterinumero: str, huippunopeus: int, tankin_koko: float):
        super().__init__(rekisterinumero, huippunopeus)
        self.tankin_koko = tankin_koko

    def __str__(self) -> str:
        return super().__str__() + '\n' + f'Auton tankin koko on: {self.tankin_koko} l'


"""sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat"""
s = Sähköauto('ABC-15', 180, 52.5)
p = Polttomoottoriauto('ACD-123', 165, 32.3)
for a in (s, p):
    a.nopeus = 123
    a.kulje(3)
    print(a.matka)
