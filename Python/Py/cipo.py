meret1 = input("Adj meg egy cipőméretet! ")
meret2 = input("Adj meg egy másik cipőméretet! ")

if meret1 > meret2:
    print("A cipő méret az első cipő esetében nagyobb, ", meret1)

elif meret2 > meret1:
    print("A cipő méret a másik cipő esetében nagyobb, ", meret2)

else:
    print("A két cipő mérete egyenlő")