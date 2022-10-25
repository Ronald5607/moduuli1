from t1 import Hissi


class Talo:

    def __init__(self, alinkerros: int, ylinkerros: int, hissien_lukumäärä: int):
        self.hissit = [Hissi(alinkerros, ylinkerros) for n in range(hissien_lukumäärä)]

    def aja_hissia(self, kerros: int, hissi: int) -> None:
        if len(self.hissit) > hissi - 1:
            self.hissit[hissi - 1].siirry_kerrokseen(kerros)

    def tulosta_hissin_kerros(self, hissi: int) -> None:
        if len(self.hissit) > hissi - 1:
            print(self.hissit[hissi - 1].kerros)

    def palohalytys(self) -> None:
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(hissi.alinkerros)


if __name__ == '__main__':
    t = Talo(0, 10, 3)
    t.aja_hissia(5, 5)
    t.aja_hissia(5, 2)
    t.tulosta_hissin_kerros(2)
    t.aja_hissia(3, 3)
    t.tulosta_hissin_kerros(3)
    t.aja_hissia(10, 1)
    t.tulosta_hissin_kerros(1)

    t.palohalytys()
    for i in range(3):
        t.tulosta_hissin_kerros(i)

