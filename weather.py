#!/usr/bin/env python3
from urllib.request import urlopen 
import json
url = "https://api.brightsky.dev/current_weather?dwd_station_id=01766"
# cf https://brightsky.dev/docs/#/operations/getCurrentWeather
# cf https://brightsky.dev/docs/#/#data-sources
response = urlopen(url) 
data = json.loads(response.read()) 
temperature = None
timestamp = None
location = None
timestamp = data['weather']['timestamp']
temperature = data['weather']['temperature']
for i in data['sources']: # key _sources_ contains a list, we have to iterate through the list
    location = (i['station_name']) 
    break
print("At ",location, "at",timestamp, "the measured temperature was ",temperature," °C")
