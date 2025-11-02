import requests
import json

city = input("Enter city: ")
state = input("Enter state(or leave it bank): ")
country = input("Enter country(ex: fin , US): ")
limit = 1
api_key = "c437454c16132e791407052d5bec8558"

request_Location = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit={limit}&appid={api_key}"

try:
    response = requests.get(request_Location)
    if response.status_code==200:
        json_response = response.json()
        for a in json_response:
            print(a["name"])

except requests.exceptions.RequestException as e:
    print ("Request could not be completed.")

lat = json_response[0]["lat"]
lon = json_response[0]["lon"]

weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
weather_data = requests.get(weather_url).json()

try:
    weather_data = requests.get(weather_url)
    if weather_data.status_code == 200:
        weather = weather_data.json()
        temp = weather["main"]["temp"]
        description = weather["weather"][0]["description"]
        print(f"Temperature: {temp}°C")
        print(f"Weather: {description}")

except requests.exceptions.RequestException as e:
    print ("Request could not be completed.")