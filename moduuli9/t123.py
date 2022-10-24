class Auto:

    def __init__(self, rekisteritunnus, huippunopeus):
        '''ekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu matka'''
        self.rekisteritunnus = rekisteritunnus
        self. huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, kiihdytys):
        self.nopeus = self.nopeus + kiihdytys
        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit

    def __str__(self):
        return f'''Auton rekisteritunnus on: {self.rekisteritunnus}
Auton huippunopeus on: {self.huippunopeus} km/h
Auton tämänhetkinen nopeus on: {self.nopeus} km/h
Auton kuljettu matka on: {self.matka} km
        '''


if __name__ == 'main':
    uusi_auto = Auto('ABC-123', 142)

    print(uusi_auto)

    '''+30 km/h, sitten +70 km/h ja lopuksi +50 km/h.'''
    for n in (30, 70, 50):
        uusi_auto.kiihdyta(n)
        uusi_auto.kulje(1)
    print(uusi_auto.nopeus, 'km/h')
    print(uusi_auto.matka, 'km')

    uusi_auto.kiihdyta(-200)
    print(uusi_auto.nopeus, 'km/h')
