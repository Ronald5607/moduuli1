s = input('Mikä on biologinen sukupuolesi (mies, nainen)? ')
he = float(input('Hemoglobiini arvosi (g/l)? '))

if s == 'mies':
    if 134 <= he <= 195:
        print('Hemoglobiini arvosi on normaali.')
    elif he < 134:
        print('Hemoglobiini arvosi on alhainen.')
    elif he > 195:
        print('Hemoglobiini arvosi on korkea.')
elif s == 'nainen':
    if 117 <= he <= 175:
        print('Hemoglobiini arvosi on normaali.')
    elif he < 117:
        print('Hemoglobiini arvosi on alhainen.')
    elif he > 175:
        print('Hemoglobiini arvosi on korkea.')