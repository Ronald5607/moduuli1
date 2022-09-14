import mysql.connector


def lentokenttatyyppi(maakoodi, yhteys):
    sql = 'select type, count(*) from airport where iso_country= "%s" group by type' % maakoodi
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos


yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='roni',
         autocommit=True
         )

maakoodi = input('Anna maakoodi: ')
a = lentokenttatyyppi('FI', yhteys)
for tulos in a:
    print(tulos[0], tulos[1], sep=', ')
