import requests as req


def naloga1(odgovor):
    if odgovor.status_code != 200:
        print("Napaka pri klicu API-ja.")
        return

    info = odgovor.json()
    tecaji = info["rates"]

    print("Tečaji na dan", info["date"])

    for valuta, tecaj in tecaji.items():
        print(valuta + ":", tecaj)

    print("Skupaj valut:", len(tecaji))


def v_tujo(evri, valuta, tecaji):
    if valuta not in tecaji:
        return None
    return evri * tecaji[valuta]


def v_evre(znesek, valuta, tecaji):
    if valuta not in tecaji:
        return None
    return znesek / tecaji[valuta]


def naloga2(odgovor):
    if odgovor.status_code != 200:
        print("Napaka pri klicu API-ja.")
        return

    tecaji = odgovor.json()["rates"]

    evri = float(input("Znesek v EUR: "))
    valuta = input("Valuta: ").upper()

    tuje = v_tujo(evri, valuta, tecaji)

    if tuje is None:
        print("Valuta", valuta, "ne obstaja.")
    else:
        print(evri, "EUR =", round(tuje, 2), valuta)
        nazaj = v_evre(tuje, valuta, tecaji)
        print(round(tuje, 2), valuta, "=", round(nazaj, 2), "EUR")


def naloga3(odgovor):
    if odgovor.status_code != 200:
        print("Napaka pri klicu API-ja.")
        return

    dnevi = odgovor.json()["rates"]
    datumi = list(dnevi.keys())

    print(datumi[0] + ":", dnevi[datumi[0]]["USD"])

    for i in range(1, len(datumi)):
        danes = dnevi[datumi[i]]["USD"]
        vceraj = dnevi[datumi[i - 1]]["USD"]

        if danes > vceraj:
            smer = "gor"
        else:
            smer = "dol"

        print(datumi[i] + ":", danes, "(" + smer + ")")

    print("Podatki od", datumi[0], "do", datumi[-1] + ", skupaj", len(datumi), "dni")


def naloga4(odgovor, valute):
    if odgovor.status_code != 200:
        print("Napaka pri klicu API-ja.")
        return

    tecaji = odgovor.json()["rates"]

    for a in valute:
        for b in valute:
            if a == b:
                continue
            tecaj = tecaji[b] / tecaji[a]
            print("1", a, "=", round(tecaj, 4), b)


def naloga5(odgovor, prihranki):
    if odgovor.status_code != 200:
        print("Napaka pri klicu API-ja.")
        return

    dnevi = odgovor.json()["rates"]

    prvi_dan = list(dnevi.keys())[0]
    najboljsi = prvi_dan
    najslabsi = prvi_dan
    vsota = 0

    for datum, tecaji_dne in dnevi.items():
        tecaj = tecaji_dne["GBP"]
        if tecaj > dnevi[najboljsi]["GBP"]:
            najboljsi = datum
        if tecaj < dnevi[najslabsi]["GBP"]:
            najslabsi = datum
        vsota = vsota + tecaj

    povprecje = vsota / len(dnevi)

    nad = 0
    for tecaji_dne in dnevi.values():
        if tecaji_dne["GBP"] > povprecje:
            nad = nad + 1

    najvec = prihranki * dnevi[najboljsi]["GBP"]
    najmanj = prihranki * dnevi[najslabsi]["GBP"]

    print("Najboljši dan:", najboljsi, "->", round(najvec, 2), "GBP")
    print("Najslabši dan:", najslabsi, "->", round(najmanj, 2), "GBP")
    print("Razlika:", round(najvec - najmanj, 2), "GBP")
    print("Povprečni tečaj:", round(povprecje, 4))
    print("Dni nad povprečjem:", nad, "od", len(dnevi))


def naloga6(odgovor, vlozek):
    if odgovor.status_code != 200:
        print("Napaka pri klicu API-ja.")
        return

    dnevi = odgovor.json()["rates"]
    datumi = list(dnevi.keys())

    najboljsi_zasluzek = 0
    dan_nakupa = None
    dan_prodaje = None

    for i in range(len(datumi)):
        for j in range(i + 1, len(datumi)):
            dolarji = v_tujo(vlozek, "USD", dnevi[datumi[i]])
            evri = v_evre(dolarji, "USD", dnevi[datumi[j]])
            zasluzek = evri - vlozek

            if zasluzek > najboljsi_zasluzek:
                najboljsi_zasluzek = zasluzek
                dan_nakupa = datumi[i]
                dan_prodaje = datumi[j]

    if dan_nakupa is None:
        print("Prijatelj nima prav.")
        return

    print("Kupi:", dan_nakupa, "(" + str(dnevi[dan_nakupa]["USD"]) + ")")
    print("Prodaj:", dan_prodaje, "(" + str(dnevi[dan_prodaje]["USD"]) + ")")
    print(vlozek, "EUR ->", round(vlozek + najboljsi_zasluzek, 2), "EUR")
    print("Zaslužek:", round(najboljsi_zasluzek, 2), "EUR")


def main():
    url = "https://api.frankfurter.dev/v1/"
    latest = url + "latest"
    september = url + "2026-09-01..2026-09-30"

    params = {"symbols": "USD,GBP,CHF,JPY"}
    odgovor = req.get(latest, params=params)
    naloga1(odgovor)

    odgovor = req.get(latest)
    naloga2(odgovor)

    odgovor = req.get(url + "2026-09-01..2026-09-07", params={"symbols": "USD"})
    naloga3(odgovor)

    valute = ["USD", "GBP", "CHF"]
    odgovor = req.get(latest, params={"symbols": ",".join(valute)})
    naloga4(odgovor, valute)

    odgovor = req.get(september, params={"symbols": "GBP"})
    naloga5(odgovor, 800)

    odgovor = req.get(september, params={"symbols": "USD"})
    naloga6(odgovor, 1000)


if __name__ == "__main__":
    main()