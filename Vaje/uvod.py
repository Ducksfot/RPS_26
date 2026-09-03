def hello():
    oddelek = input("Kateri oddelek si?: ")
    if oddelek.lower() == "1.ri":
        print(f"Hello {oddelek}♡")
    else:
        print(f"Hello {oddelek}")

def poštevanka():
    x = int(input("Izberi si število: "))
    st = 1

    while st <= 10:
        print(f"{st} * {x} = {st * x}")
        st += 1

if __name__ == "__main__":
    # Hello()
    poštevanka()
