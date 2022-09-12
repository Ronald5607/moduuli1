import math
#kuukaudet = ('Talvi','Talvi','Kevät',
#             'Kevät','Kevät','Kesä',
#             'Kesä','Kesä','Syksy',
#             'Syksy','Syksy','Talvi')
kuukaudet = ('Talvi', 'Kevät', 'Kesä', 'Syksy', 'Talvi')

a = [math.ceil(x/3) for x in range(12)]

kuukausi = int(input('Mikä kuukausi: '))

if 0 < kuukausi <= 12:
    print(f'Kuukausi {kuukausi} kuuluu vuodenaikaan {kuukaudet[a[kuukausi-2]]}.')
else:
    print('Ei ole kuukausi.')


