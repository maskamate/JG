def meretek(meret):
    if (meret > 41):
        return True
    else:
        return False

while True:
    nev = input("Add meg a cipőt használó nevét! ")
    if (nev == ""):
        break

    meret = int(input("Adj meg egy cipőméretet! "))
    if meretek(meret):
        print(nev, "nagy lábon él")

    else:
        print(nev, "kis lábon él")