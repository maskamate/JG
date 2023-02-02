# KÉRJE BE KÉT HAJÓ SEBESSÉGÉT ÁS ÁLLAPÍTSA MEG, HOGY MELYIK A GYORSABB

hajo1 = input("Kérem adja meg a hajó sebességét: ")
hajo2 = input("Kérem adja meg a hajó sebességét: ")


if hajo1 > hajo2:
    print("Az első hajó sebessége nagyobb")

elif hajo2 > hajo1:
    print("A második hajó sebessége nagyobb")

else:
    print("A két hajó sebessége ugyan akkora")


# ÍRJON FÜGGVÉNY, AMELY ÁTVÁLTJA A CSOMÓT, KM/H-RA | 1 CSOMÓ = 1.852 KM/H
def valto(sebesseg):
    return sebesseg*1.852