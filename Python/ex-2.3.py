# Esercizio 2.3 - Dizionari e Tuple
"""
Modificare la soluzione delle liste in modo da utilizzare un dizionario invece della lista e una tupla per rappresentare la data. Stampare a video un messaggio del tipo:
Struttura dati: {'Nome': 'Stefano', 'Data': (10, 'Ottobre', 1994)}

Suggerimento: Leggete 
- http://www.html.it/pag/15614/dizionari/
- http://www.html.it/pag/15615/tuple/
"""


nn = input("inserisci il tuo nome: ")
dd = int(input("Il giorno in cui sei nato: "))
mm = input("Il mese in cui sei nato: ")
aa = int(input("L'anno in cui sei nato: "))

data = (dd, mm, aa)
persona = {"Nome": nn}
persona.update({"Data": data})
print(persona)