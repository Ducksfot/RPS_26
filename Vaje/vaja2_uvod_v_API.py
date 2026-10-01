import requests as req 

url = "https://api.open-meteo.com/v1/forecast?latitude=46.2389&longitude=14.3556&current=temperature_2m&forecast_days=1"

klic = req.get(url)
klicJSON = klic.json()
print(klicJSON["current"]["temperature_2m"])
