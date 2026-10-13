# naloga 1

import requests

url = "https://api.frankfurter.dev/v1/latest"
odg = requests.get(url, params={"symbols": "USD,GBP,CHF,JPY"})

if odg.status_code != 200:
    print(f"Napaka pri klicu API-ja.")
else:
    pass

podatki = odg.json()
tecaji = podatki["rates"]

print("Tečaji na dan", podatki["date"])

for valuta, tecaj in tecaji.items():
    print(valuta + ":", tecaj)

print("Skupaj valut:", len(tecaji))