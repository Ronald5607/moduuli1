from random import randint

n = randint(1, 10)
arvaus = 0

while arvaus != n:
    arvaus = int(input('Arvaa kokonaisluku väliltä 1-10: '))
    if arvaus < n:
        print('Väärin! vastauksesi oli liian pieni.')
    if arvaus > n:
        print('Väärin! vastauksesi oli liian suuri.')

print(f'{n} oli oikea vastaus!')