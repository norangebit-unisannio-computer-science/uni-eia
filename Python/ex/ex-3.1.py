# EIA 2018 - Esercizio 3.1

"""
Leggete in memoria i dati che avete salvato nell'esercizio precedente.

Utilizzando la comprehension, ricercate i nominativi che iniziano con una specifica lettera e stampate a video i relativi record.

HINT: Guardate
http://www.html.it/pag/40150/comprehension-per-liste-e-dizionari/
"""
persone = []   
f = open ('file/ex-2.4.txt', 'r')
while True:
    nn=f.readline();
    if(nn==''):
        break;
    dd=int(f.readline())
    mm=f.readline()
    aa=int(f.readline())
    data = (dd, mm, aa)
    persona ={"Nome": nn, "Data": data}
    persone.append(persona)

f.close();

c = input("Inserisci una lettera: ")

persone = [p for p in persone if p.get("Nome")[0]==c]
print(persone)

