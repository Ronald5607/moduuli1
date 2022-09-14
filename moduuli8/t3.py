import mysql.connector
from geopy.distance import distance


def lentokentta(icao, yhteys):
    sql = 'SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s' % icao
    kursori = yhteys.cursor(buffered=True)
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

a = lentokentta(input('Anna ensimmäisen lentokentän ICAO-koodi: '), yhteys)
b = lentokentta(input('Anna toisen lentokentän ICAO-koodi: '), yhteys)
print(a)
print(b)
if a and b:
    print(distance(a, b))