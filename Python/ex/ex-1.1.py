# EIA 2018 - ESERCIZIO 1.1
"""
Correggere gli errori contenuti nel codice

Nota:
Gli input al file sono forniti attraverso il file Stdin
che torvate nella tab in alto.
Nel file va inserita la sequenza di input prevista, 
compreso il carattere di invio.
"""

valore = float(input('Inserisci un valore: '))
if valore > 0:
    print ("positivo")
elif valore < 0:
    print("negativo")
else:
    print ("nullo")
