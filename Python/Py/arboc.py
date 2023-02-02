def arboc(magassag):
    return magassag/100
def kapnev(nev):
    return nev.title()

h = int(input("Kérem adja meg az árbóc hosszusagat (cm): "))
nev = input("Kapitány neve: ")
print(arboc(h))
print(kapnev(nev))