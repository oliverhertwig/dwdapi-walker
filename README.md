**A very simple and unsophisticated proof-of-concept for using the**
[Bright Sky API](https://github.com/jdemaeyer/brightsky)

- weather.py calls the (https://api.brightsky.dev/current_weather) API endpoint for a predefined DWD weather station and extracts
timestamp, station name and temperature reading from the resulting json answer.
- psweather.ps1 does more or less the same in Powershell 7. Please note, that the example includes a shebang for PS on Linux. For usage in a MS Windows environment, this has to be adapted.
- Both code examples do not reflect the usage of a proxy. 
- exmpl_shrt.json and exmpl_lng.json are for local testing without bothering the API

  This code comes with absolutely no warranty. Use it as you see fit, the MIT License should be permissive enough.
  Please be aware that I might not be very active here. 

