# EIA 2018 - ESERCIZIO 1.2
"""
Scrivere un programma Python che calcoli il valore della merce, conoscendo prezzo e quantita'.

Chiedere di inserire il nome della merce "n"
Chiedere di inserire la quantita' "q".
Chiedere di inserire il prezzo "p".
Calcolare il valore "v = p*q".

Risultati attesi:

TEST CASE 1
Nome della merce da acquistare: Cavi
Quantita' di merce da acquistare: 10
Prezzo unitario della merce: 5
Grazie. Il valore della merce "Cavi" ammonta a 50 

TEST CASE 2
Nome della merce da acquistare: Alimentatori
Quantita' di merce da acquistare: 34
Prezzo unitario della merce: 12.30
Grazie. Il valore della merce "Alimentatori" ammonta a 418.2
"""
    
n = input("Nome della merce da acquistare: ")
q = float(input ("Quantita' di merce da acquistare: "))
p = float(input ("Prezzo unitario della merce: "))

v = p*q

print('Grazie. Il valore della merce "', n, '" ammonta a', v)
