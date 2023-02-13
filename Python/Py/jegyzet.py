nev=input('Mi legyen a neve a fájlnak? ')
x=None
lista=[]

wr=open('H:\\jegyzet.txt','w')
wr.write(f'A fájl neve: {nev}\n',)
wr.write(f'A fálj megtalálható a H meghajtóban!\n')
while x !='stop':
    x=input('Írj amit szeretnél. Ha be akarod fejezni az írást írd be hogy stop. ')
    lista.append(x)
    
for listak in lista:
    print(listak)
    wr.write(f'{listak}\n')