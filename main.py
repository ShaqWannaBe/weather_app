"""

This app will query a weather API to find data about the weather.
Then it will notify users of the weather.

"""

#import pyowm.owm import OWM
import requests
import json

api_key = '22eca9c04a24c301da463fa57a955b0a'
lat = '33.293160'
lon = '-112.037024'

url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly&appid={api_key}'

res = requests.get(url)
data = res.json

temp = data['current']['temperature']

print(temp)




