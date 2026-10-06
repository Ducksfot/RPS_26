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
