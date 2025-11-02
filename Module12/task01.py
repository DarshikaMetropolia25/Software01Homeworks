import requests
import json

keyword = input("press C and Enter to get a Random Chuck Norris Joke: ")

# Request template: https://api.tvmaze.com/search/shows?q=girls
request = "https://api.chucknorris.io/jokes/random"
response = requests.get(request).json()
print(json.dumps(response["value"]))
