#!/usr/bin/env python3
# import urllib3
# from urllib.request import urlopen 
import json
# http = urllib3.PoolManager()
# site = http.request("get", "https://api.brightsky.dev/weather?dwd_station_id=06313&date=2024-07-01").data
# url = "https://api.brightsky.dev/weather?dwd_station_id=06313&date=2024-07-01"
# response = urlopen(url) 
# data = json.loads(response.read()) 
# data = json.loads(site)
# print(data)
with open('dreck.json','r') as f:
    data = json.load(f)
    print(type(data))
    print(data.keys())
    print(data.values())
    # oli = data.get("id")
    # print(oli)
    # test = data['weather']
    # getting hold of the values of 
    # variableParam
    # test1 = test[0].values()  
    # list(test.values())
    # print(test1)
    # test2 = list(test1)[0]
    # test3 = test2[1:-1].split(",")
    # print(test3[1])
    print("mee")
