# ESERCIZIO 2.2 - Liste
"""
Modificare la soluzione delle esercizio sulle stringhe in modo che i dati vengano inseriti nella lista LS e da lì recuperati per essere mostrati a video. 

Stampare in coda un messaggio che mostri LS. Ad esempio:
Struttura dati: ['Stefano',[10,'Ottobre',1994]]

Suggerimento: Leggete
- http://www.html.it/pag/15613/liste/
"""

nn = input("inserisci il tuo nome: ")
dd = int(input("Il giorno in cui sei nato: "))
mm = input("Il mese in cui sei nato: ")
aa = int(input("L'anno in cui sei nato: "))

data = [dd, mm, aa]
persona = [nn]
persona.append(data)
print(persona)