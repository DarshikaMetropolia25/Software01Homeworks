from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='userdarshika',
    password='ADIL2022',
    autocommit=True
)

@app.route('/airport/<icao_code>')
def get_airport_Name_and_Location(icao_code):
    sql = (
        f"SELECT airport.name, airport.municipality "
        f"FROM airport WHERE airport.ident='{icao_code}'"
    )

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    if cursor.rowcount > 0:
        name = result[0][0]
        location = result[0][1]
        response = {
            "ICAO": icao_code,
            "Name": name,
            "Location": location
        }
    else:
        response = {"error": "Airport not found"}

    return jsonify(response)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
