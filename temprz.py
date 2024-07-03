#!/usr/bin/env python3
from urllib.request import urlopen 
import json
# 06313 Breckerfeld Wengeberg 03098 Luedenscheid 01766 Muenster/Osnabrueck
# cf https://brightsky.dev/docs/#/#data-sources
url = "https://api.brightsky.dev/current_weather?dwd_station_id=01766&date=2024-07-01"
# cf https://brightsky.dev/docs/#/operations/getCurrentWeather
response = urlopen(url) 
data = json.loads(response.read()) 
time = None
temp = None
loc = None
time = data['weather']['timestamp'] 
temp = data['weather']['temperature']
#loc = data['sources']['station_name']
loc = "depp"
print("Am ", time, "wurde am Standort ", loc, "eine Temperatur von ", temp, "gemessen.")
