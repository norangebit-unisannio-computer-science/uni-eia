# EIA 2018 - Esercizio 3.3
"""
Modificare l'esercizio Funzioni introducendo la classe Persona che abbia come attributi nome e data di nascita. 
Invece del dizionario, la funzione crea l'istanza di  Persona.

HINT:
http://www.html.it/pag/15621/classi-e-cenni-di-programmazione-ad-oggetti/
http://www.html.it/pag/15622/classi-in-python/
"""

class persona:
    nn = ''
    dd = ''
    mm = ''
    aa = ''

    def __init__(self, nn, dd, mm, aa):
        self.nn = nn
        self.dd = dd
        self.mm = mm
        self.aa = aa

    def stampa(self):
        print(self.nn,self.dd,self.mm,self.aa)

def diz(f):
    nn=f.readline();
    if(nn==''):
        return
    dd=int(f.readline())
    mm=f.readline()
    aa=int(f.readline())
    data = (dd, mm, aa)
    return persona(nn, dd, mm, aa)


persone = []   
f = open ('file/ex-2.4.txt', 'r')
p=diz(f)
while p!=None:
    persone.append(p)
    p=diz(f)

f.close();

for p in persone:
    p.stampa()