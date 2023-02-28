szavak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']
t_szavak = []
for szo in szavak:
   if szo[0]=="t" or szo[0]=="T":
      print(szo)
      t_szavak.append(szo)

print("A t betűs szavak: ", t_szavak)