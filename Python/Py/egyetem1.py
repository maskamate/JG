class HíresEgyetem:
    def __init__(self, nev, varos, nemzetiseg):
        self.nev = nev
        self.varos = varos
        self.nemzetiseg = nemzetiseg

    def elotag(self):
        if self.nemzetiseg == "a":
            return "angol"
        else:
            return "német"

    egyetemek=[]
    for _ in range(3):
        nev=input("add meg  nevet: ")
        varos=input("add meg a varost: ")
        nemzetiseg=input("add meg a nemzetiseget (a/n): ")
        iskola = HíresEgyetem(nev, varos, nemzetiseg)
        egyetemek.append(suli)
    for iskola in egyetemek:
        print(f'az egyetem neve: ', {iskola.nev}, 'amely', {iskola.varos}, '-ban van, egy híres iskola', {iskola})

