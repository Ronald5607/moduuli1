from flask import Flask, request
import mysql.connector

app = Flask(__name__)

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='roni',
         autocommit=True
         )


@app.route('/alkuluku/<luku>')
def alkuluku(luku) -> dict:

    balkuluku = True

    luku = int(luku)

    for i in range(2, luku):
        if luku % i == 0:
            balkuluku = False

    if balkuluku and luku > 1:
        return {
            'number': luku,
            'isprime': True

        }
    else:
        return {
            'number': luku,
            'isprime': False
        }


@app.route('/kenttä/<ICAO>')
def kenttä(ICAO):
    sql = 'SELECT ident, name, municipality FROM airport WHERE ident = \"%s\"' % ICAO
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()

    try:
        return {
            'ICAO': tulos[0],
            'Name': tulos[1],
            'Municipality': tulos[2]
        }
    except IndexError:
        return 'Ei löytynyt.'
    except TypeError:
        return 'Ei löytynyt.'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, use_reloader=True)
