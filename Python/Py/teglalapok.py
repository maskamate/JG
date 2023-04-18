def b_oldal(teglalap):
    return teglalap

teglalap = [[1,9], [2,3], [5,7]]

print(max(teglalap))
print(max(teglalap, key = b_oldal))

print(max(teglalap.key = lambda teglalap:teglalap[1]))
print(max(teglalap.key = lambda tl:tl[0] *tl[1]))

koszont = lambda vezetéknév, keresztnév, szia = {vezetéknév}{keresztnév}
