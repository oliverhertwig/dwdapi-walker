#!/usr/bin/env pwsh
try
{
    $data = Invoke-WebRequest -Uri "https://api.brightsky.dev/current_weather?dwd_station_id=01766"|convertfrom-json
    # cf https://brightsky.dev/docs/#/#data-sources
    # cf https://brightsky.dev/docs/#/operations/getCurrentWeather
    # dwd_station_id 01766 is Muenster/Osnabrueck Airport
    $StatusCode = $data.StatusCode
} catch {
    $StatusCode = $_.Exception.Response.StatusCode.value__
}
$timestamp = $data.weather.timestamp
$temperature = $data.weather.temperature 
write-host "At Muenster/Osnabrueck Airport at $timestamp measured temp was:  $temperature °C"
