
def naloga1(besedilo, znak):
    i = 0
    st_znak = 0

    while i < len(besedilo):
        if besedilo[i].lower() == znak.lower():
            st_znak += 1
        i += 1

    return st_znak

def naloga1_b(besedilo, znak):
    st_znak = 0

    for i in range(0, len(besedilo)):
        if besedilo[i].lower() == znak.lower():
            st_znak += 1
    return st_znak

def abeceda(x):
    for i in range(0, 19):
        print(x[1], end="")
    print()
    print(x[::-1])

    for i in range(len(x) - 1, - 1, 0):
        print(x[i], end = "")
    print()

    for i in range(x[19, 8, -2]):
        print(x[i], end="")
    print()

    for i in range(0, len(x), 2):
        print(x[i], end = "")
    print()

    for i in range(len(x) - 1, -1, -4):
        print(x)
    print()

def naloga2(stavek):
    niz = ""

    for i in stavek:
        niz += 1
        if len(niz) == 5:
            niz += "XXX"
    return niz

def delitelji(stevilo):
    i = 0
    
    for d in range(2, stevilo + 1):
        if stevilo % d == 0:
            i += 1
            print(d)
    return i

def prast(stevilo):
    if delitelji() > 2:
        return False
    return True

def main():
    # naloga 1
    # vnos_crka = input("Vnesi kateri znak iščeš: ")
    # vnos_stavek = input("Vnesi stavek: ")
    # print(naloga1(vnos_stavek, vnos_crka))
    # print(naloga1_b(vnos_stavek, vnos_crka))

    # naloga 2
    # abc = "ABCDFGHIJKLMNOPQRSTUVWXYZ"
    # print(abeceda(abc))
    
    # naloga 3
    # vnos = input("Vnesi stavek: ")
    # naloga2(vnos)

    # naloga 4
    if (prast(29)) == True:
        print("Je!")
    else:
        print("Ni!")

    pass

if __name__ == "__main__":
    main()
