from cipő_alap import Cipő

tarolas = []

for _ in range(1):
    ringli = input("Add meg egy cipő ringli számát! ")
    anyag = input("Add meg a cipő anyagát (bőr -b; Mesterséges anyag – m)! ")
    meret = input("Add meg a cipő méret! ")
    nem = None

    cipő = Cipő(ringli, anyag, meret, nem)
    tarolas.append(cipő)

    if   "35" < meret < "41":
        nem = "női méret"
    elif meret > "41":
        nem = "férfi méret"

    if anyag == "b":
        anyag = "Bőr"
    elif anyag == "m":
        anyag = "Mesterséges anyag"

    

    for i in tarolas:
        print("A cipő ringli száma: ", ringli, "és ", anyag, "-ból/ből készült. Ez a cipő ", meret, "méret, valamint ", nem)