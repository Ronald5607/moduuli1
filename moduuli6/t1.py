from random import randint

def nopanheitto():
    return randint(1,6)

n = 0
while n != 6:
    n = nopanheitto()
    print(n)
