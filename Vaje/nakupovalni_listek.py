def vnos(s:list):
    while True:
        izdelek = input("Vnesi: ")
        if izdelek == "":
            break
        s.append(izdelek)

def izpis(s:list):
    print("---------------------------------")
    for index in range(len(s)):
        
        print(f"{[index+1]} {s[index]}")

def briši(s:list):
    briši = input("Briši: ")

    print("Brišem: ", end = "")

    while briši in s:
        s.remove(briši)
        print("*", end = "")
    print()

def posodobi(s:list):

    stara = input(f"Posodobi: ").lower()
    nova = input(f"Novo: ").lower()

    for index in range(len(s)):
        if stara == s[index]:
            s[index] = nova


if __name__ == "__main__":
    db = []
    vnos(db)
    izpis(db)
    briši(db)
    izpis(db)
    posodobi(db)
    izpis(db)