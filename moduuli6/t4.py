def summa(lista):
    fsumma = 0
    for n in lista:
        fsumma += n
    return fsumma


Tlista = [x for x in range(25)]
print(summa(Tlista))