import mysql.connector

def get_airport_Name_and_Location(area_code):
    sql = f"SELECT airport.name, airport.type FROM airport WHERE airport.iso_country = '{area_code}' ORDER BY airport.type ASC;"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0 :
        for row in result:
            print(f"Airport {row[0]} is a {row[1]} ")
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

area_code = input("Enter area_code: ")
get_airport_Name_and_Location(area_code)