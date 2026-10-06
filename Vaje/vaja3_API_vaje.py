
import requests

# mini vaja 1
avto = {
    "znamka": "Renault",
    "model": "Clio",
    "letnik": 2020
}

print(avto["model"])

avto["barva"] = "modra"

for kljuc, vrednost in avto.items():
    print(f"{kljuc}: {vrednost}")

# mini vaja 2
sola = {
    "ime": "ŠC Kranj",
    "naslov": {
        "ulica": "Kidričeva cesta 55",
        "posta": 4000,
        "kraj": "Kranj"
    },
    "smeri": ["računalništvo", "elektrotehnika", "mehatronika"]
}

print(sola["naslov"]["posta"])   


print(", ".join(sola["smeri"]))

#mini vaja 3
import requests

def trenutna_temperatura(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    parametri = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m"
    }
    odgovor = requests.get(url, params=parametri)
    podatki = odgovor.json()
    return podatki["current"]["temperature_2m"]


kraji = {
    "Ljubljana": (46.0569, 14.5058),
    "Maribor": (46.5547, 15.6459),
}

for ime, (lat, lon) in kraji.items():
    t = trenutna_temperatura(lat, lon)
    print(f"{ime}: {t} °C")
