def kis_nagy(letszam):
    if letszam>=1000:
        return True
    else:
        return False
   
iskola=None
letszam=None
while iskola!='':
    iskola=input('Add meg az iskola nevét! ')
    if iskola=='':
        break
    letszam=int(input('Add meg a létszámát!'))
    if kis_nagy(letszam)==True:
        print(iskola,' nagy létszámú iskola.')
    else:
        print(iskola,' kis létszámú iskola.')