#!/usr/bin/env python3
#import urllib3
from urllib.request import urlopen 
import json
# http = urllib3.PoolManager()
# site = http.request("get", "https://api.brightsky.dev/weather?dwd_station_id=06313&date=2024-07-01").data
# url = "https://api.brightsky.dev/weather?dwd_station_id=06313&date=2024-07-01"
# 06313 Breckerfeld Wengeberg 03098 Luedenscheid 01766 Muenster/Osnabrueck
url = "https://api.brightsky.dev/current_weather?dwd_station_id=01766&date=2024-07-01"
response = urlopen(url) 
data = json.loads(response.read()) 
# print(data)
# for testimg purposes use downloaded json file
# with open('exmpl_shrt.json','r') as f:
    #data = json.load(f)
    #print(type(data))
    #print(data.keys())
    # print(data.values())
w = None
w = data['weather']['temperature']
print(w) # val1
i = None
s = None
for i in data['sources']:
    print(i['station_name'])
    s = (i['station_name'])
    print(s)
    #break
    continue
    print(s)
