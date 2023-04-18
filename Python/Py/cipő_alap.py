class Cipő:
    def __init__(self,ringli,anyag,meret,nem):
        self.ringli = ringli
        self.anyag = anyag
        self.meret = meret
        self.nem = nem
 # http://www.cipeszmester.hu/cipofuzok/cipofuzo
        if ringli == 2:
            return(f'Kicsi: 45,Közepes: 75,Nagy: 75')
        elif ringli == 3:
            return(f'Kicsi: 60,Közepes: 75,Nagy: 90')