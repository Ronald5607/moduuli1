
class Hissi:

    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.kerros = self.alinkerros

    def kerros_alas(self) -> None:
        self.kerros = self.kerros - 1 if self.kerros > self.alinkerros else self.alinkerros

    def kerros_ylös(self) -> None:
        self.kerros = self.kerros + 1 if self.kerros < self.ylinkerros else self.ylinkerros

    def siirry_kerrokseen(self, kerros: int) -> None:
        # if kerros < self.alinkerros or kerros > self.ylinkerros:
        #     raise ValueError('Antamasi kerros on liian pieni tai suuri.')
        if kerros > self.kerros:
            for i in range(kerros - self.kerros):
                self.kerros_ylös()
        else:
            for i in range(self.kerros - kerros):
                self.kerros_alas()


if __name__ == '__main__':
    h = Hissi(0, 10)
    h.siirry_kerrokseen(5)
    print(h.kerros)
    h.siirry_kerrokseen(5)
    print(h.kerros)
    h.siirry_kerrokseen(7)
    print(h.kerros)
    h.siirry_kerrokseen(3)
    print(h.kerros)
    h.siirry_kerrokseen(2)
    print(h.kerros)
    h.siirry_kerrokseen(0)
