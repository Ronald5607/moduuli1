k = 'python'
s = 'rules'
kk = sk = ''

while kk != k and sk != s:
    kk = input('Anna käyttäjänimi: ')
    sk = input ('Anna salasana: ')
    if kk != k and sk != s:
        print('Pääsy evätty.')

print('Tervetuloa')