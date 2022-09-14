import mysql.connector


def lentokentta(icao, yhteys):
    sql = 'SELECT name, municipality FROM airport WHERE ident = %s' % icao
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    return tulos




yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='roni',
         autocommit=True
         )
icao = input('Anna ICAO koodi: ')
a = lentokentta(icao, yhteys)
if a:
    print(a[0], a[1], sep=', ')
else:
    print('Ei ole lentokentän ICAO koodi.')
