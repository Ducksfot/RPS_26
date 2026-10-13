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

print(f"Tečaji na dan", {podatki["date"]})

for valuta, tecaj in tecaji.items():
    print(valuta + ":", tecaj)

print("Skupaj:", len(tecaji))

print("---------------------------------------")

import requests

podatki = odg.json()
tecaji = podatki["rates"]

def v_tujo(evri, valuta, tecaji):

    if valuta not in tecaji:
        return None
    return evri * tecaji[valuta]

def v_evre(znesek, valuta, tecaji):

    if valuta not in tecaji:
        return None
    return znesek / tecaji[valuta]

def main():

    #v_tujo
    vnos1 = float(input("Vnesi število €: "))
    vnos2 = str(input("Vnesi valuto: "))
    vnos3 = podatki["rates"]
    v_tujo(vnos1, vnos2, vnos3)

    #v_evro
    vnos1 = float(input("Vnesi število: "))
    vnos2 = str(input("Vnesi valuto: "))
    vnos3 = podatki["rates"]
    v_evre(vnos1, vnos2, vnos3)

    tuje = v_tujo(vnos1, vnos2, vnos3)

    if tuje is None:
        print("Valuta", vnos2, "ne obstaja.")
    else:
        print(vnos1, "EUR =", round(tuje, 2), vnos2)    
        nazaj = v_evre(tuje, vnos2, tecaji)
        print(round(tuje, 2), vnos2, "=", round(nazaj, 2), "EUR")

if __name__ == "main":
    main()


