# lib

import random

def naloga1(x, y):

    skupaj = x + y
    
    print(f"Zapisničar se je zmotil! Spodaj so popravljeni rezulatati:")

    print(f"Domači: {y}")
    print(f"Gostje: {x}")
    print(f"Popravljen rezultat: {y} : {x}")
    print(f"Skupaj: {skupaj}")
    
def naloga2(x):

    dnevi = x//1440
    ure = (x % 1440) // 60
    minute = x % 60

    print(f"{dnevi} dni, {ure} ur, {minute} minut.")

def naloga3(x, y):

    pice = round((x + 2) // 3)
    sum = pice * y
    na_dijaka = sum/x

    print(f"Pice: {pice}")
    print(f"Skupaj: {sum}")
    print(f"Na dijaka: {na_dijaka}")

def naloga4(x, y):

    cena = 0

    if x < 0 or x == 0:
        print(f"Neveljavna starost.")
    else:
        if y == "torek":
            cena = - 2
        if x <= 5:
            cena = "brezplačno"
        elif x > 6 and x <= 17:
            cena = cena + 5
        elif x > 18 and x <= 64:
            cena = cena + 8
        else:
            cena = cena + 6
    
    print(f"{cena} €")

def naloga5(x):

    skupaj = 0
    prvi_dan = 0

    for dan in range(1, x + 1):
        if dan % 7 != 0:
            skupaj += dan

        if skupaj > 1000 and prvi_dan == 0:
            prvi_dan = dan

    print("Prihranjeno:", skupaj, "EUR")

    if prvi_dan != 0:
        print("Več kot 1000 EUR prvič na dan:", prvi_dan)
    else:
        print("Več kot 1000 EUR še nisi prihranil.")

def naloga6(n_st):
    pass

def main():
    pass

    # naloga 1
    # doma = int(input("Vnesi št. golov domačih"))
    # gostje = int(input("Vnesi št. golov domačih"))
    # naloga1(doma,gostje)

    # naloga 2
    # minute = int(input("Vnesi minute igre: "))
    # naloga2(minute)

    # naloga 3
    # st_dijakov = int(input("Vnesi št. dijakov: "))
    # cena_pice = float(input("Vnesi ceno pice: "))
    # naloga3(st_dijakov, cena_pice)

    # naloga 4
    # starost = int(input("Vnesi svojo starost: "))
    # dan = input("Vnesi dan v tednu: ")
    # naloga4(starost, dan)

    # naloga 5
    # st_dni = int(input("Vnesi št. dni: "))
    # naloga5(st_dni)

    # naloga 6
    # nakl_st = random.randint(0, 100)
    # naloga6(nakl_st)

if __name__ == "__main__":
    main()