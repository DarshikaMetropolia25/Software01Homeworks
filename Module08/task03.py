from geopy.distance import geodesic
import mysql.connector

def measure_distance(city1,city2):
    sql = f"SELECT airport.latitude_deg, airport.longitude_deg FROM airport WHERE airport.ident='{city1}'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0 :
        for row in result:
            city1_cord=row[0],row[1]
            print(f"Airport 1 cordinates are {city1_cord} ")
    sql = f"SELECT airport.latitude_deg, airport.longitude_deg FROM airport WHERE airport.ident='{city2}'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            city2_cord = row[0], row[1]
            print(f"Airport 2 cordinates are {city2_cord} ")

    Distance=(geodesic(city1_cord,city2_cord))
    print(f"Distance between airports is {Distance} ")
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

city1 = input("Enter the first city ICAO code: ")
city2 = input("Enter the second city ICAO code: ")
measure_distance(city1,city2)