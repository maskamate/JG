class Hajo:
    def __init__(self, nev, kapnev, arboc, sebesseg, orszag):
        self.nev = nev
        self.kapnev = kapnev
        self.arboc = arboc
        self.sebesseg = sebesseg
        self.orszag = orszag


def valto(sebesseg):
    return sebesseg*1.852

def arboc(magassag):
    return magassag/100

def kapnev(nev):
    return nev.title()

def nemzet(orszag):
    if orszag == "o":
        return "orosz"
    elif orszag == "j":
        return "japán"

hajo =[]
for _ in range(3):
    hajo1 = input("Kérem adja meg a hajó sebességét: ")
    hajo2 = input("Kérem adja meg a hajó sebességét: ")
    h = int(input("Kérem adja meg az árbóc hosszusagat (cm): "))
    nev = input("Kapitány neve: ")
    orszaga = input("adja meg a hajó országát (a/o)")
    sello = Hajo(nev, kapnev,  h, sebesseg=, orszaga)
    hajo.append()

for hajok in hajo:
    print(hajok().neve, "sebessége: ", hajok().valto())

       