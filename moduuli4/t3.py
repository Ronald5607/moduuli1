i = '1'
hi = 0
lo = 0

while i:
    i = input('Anna numero: ')
    if i:
        n = float(i)
        if n < lo:
            lo = n
        if n > hi:
            hi = n

print(f'Pienin luku oli {lo} ja suurin oli {hi}.')