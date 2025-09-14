import mysql.connector

def get_airport_Name_and_Location(icao_code):
    sql = f"SELECT airport.name, airport.municipality FROM airport WHERE airport.ident='{icao_code}'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0 :
        for row in result:
            print(f"Airport name for ICAO code is {row[0]} located in {row[1]} ")
    return

# Main program
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='userdarshika',
         password='ADIL2022',
         autocommit=True
         )

icao_code = input("Enter icao_code: ")
get_airport_Name_and_Location(icao_code)