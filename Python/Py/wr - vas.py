wr=open('./nevek.txt','r')
lista=[]
wr.read()
for i in range(10):
    az=input('Adja meg a személyazonosító számát! ')
    összeg=[]
    részösszeg=None
    lista.append(az)
    print(lista)
    if lista[0] ==2 or 4:
        for i in range(10,0,1):
            for j in lista:
                részösszeg=i*j
                összeg.append(részösszeg)
                code=sum(összeg)%11
                print(részösszeg)
                print(code)
wr.close