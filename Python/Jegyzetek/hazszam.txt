def hazszam(szam):
    if szam % 2 ==0:
        return True
    else:
        return False

utca = None
szam = None
while utca != '':
    utca = input("Kérem adja meg az utca nevét! ")
    if utca == '':
        break
    szam = int(input("Kérem adja meg a ház házszámát! "))
    if hazszam(szam) == True:
        print(f'A(z) {utca} utcán a(z) {szam} számmal ellátott ház a jobb oldalt van')
    else:
        print(f'A(z) {utca} utcán a(z) {szam} számmal ellátott ház a bal oldalt van')