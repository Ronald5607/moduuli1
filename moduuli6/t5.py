def pari(lista):
    return [x for x in lista if x % 2 == 0]


kokonaislista = [x for x in range(-10, 11)]
print(kokonaislista)
print(pari(kokonaislista))
