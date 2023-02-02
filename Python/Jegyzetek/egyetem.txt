class Híres_Egyetem:
    def __init__(self, neve, varos, nemzetiseg):
        self.neve = neve
        self.varos = varos
        self.nemzetiseg = nemzetiseg
    def elotag(self):
        if self.nemzetiseg:
            return "angol"
        else:
            return "német"
         
egyetem = []
for _ in range(1):
    neve = input("Add meg egy egyetem nevét! ")    
    varos = input("Add meg a az egyetem városát! ")
    nemzetiseg = input("Add meg a nemzetiségét (a/n) ")
    if nemzetiseg == "a":
        print("University. ", neve, "egy híres amerikai egyetem, amely", varos, "-ban/ben található")
    elif nemzetiseg == "n":
        print("Universität", neve, "egy híres német egyetem, amely", varos,"-ban/ben található")