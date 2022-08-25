import random

print(f'Kolminumeroinen koodi: {str(random.randint(1000,9999))[1 : : ]}')

print(f'Nelinumeroinen koodi numerot väliltä 1-6:{random.randint(1,6)}{random.randint(1,6)}{random.randint(1,6)}{random.randint(1,6)}')