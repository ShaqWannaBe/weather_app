"""

This app will query a weather API to find data about the weather.
Then it will notify users of the weather.

"""

import requests
import json

api_key = '22eca9c04a24c301da463fa57a955b0a'
lat = '33.293160'
lon = '-112.037024'
units = 'imperial'      # Use either metric or imperial

url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units={units}&exclude=minutely,hourly&appid={api_key}'

res = requests.get(url)
data = res.json()

#prints the result of the api call
#print(data)

#round the current temp and turn it into an integer
temp = int(round(data['current']['temp'],0))
feels_like = (int(round(data['current']['feels_like'])))
condition = data['current']['weather']

#print welcome
print('*** WELCOME TO THE WEATHER APP ***')
print('* Current Temp: ' + str(temp) + ' °F')
print('* Feels like: ' + str(feels_like) + ' °F')



