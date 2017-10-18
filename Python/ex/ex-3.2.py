# EIA 2018 - Esercizio 3.2

"""
Scrivere una funzione che dopo aver letto nome, giorno, mese e anno di nascita, restituisca un dizionario contente nome e data di nascita. 
Se il nome è vuoto, la funzione si interrompe e restituisce un valore vuoto.

Utilizzare la funzione per leggere una serie di utenti e inserirli in una lista.

HINT: http://www.html.it/pag/15618/funzioni/
"""

def diz(f):
    nn=f.readline();
    if(nn==''):
        return
    dd=int(f.readline())
    mm=f.readline()
    aa=int(f.readline())
    data = (dd, mm, aa)
    return {"Nome": nn, "Data": data}


persone = []   
f = open ('file/ex-2.4.txt', 'r')
p=diz(f)
while p!=None:
    persone.append(p)
    p=diz(f)

f.close();

print(persone)
