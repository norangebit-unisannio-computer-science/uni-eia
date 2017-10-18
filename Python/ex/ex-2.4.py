# Esercizio 2.4 - Cicli e File
"""
Con riferimento all'esercizio precedente,  scrivere un programma che chiede di inserire nominativi con data di nascita in memoria e di salvarli successivamente in un file di testo.
L'inserimento continua fino a quando on viene inserito un nominativo vuoto.

Per i record utilizzate il formato che volete. Se ci riuscite provate a salvare e a leggere direttamente nel formato della struttura di appoggio utilizza (es. lista o dizionario).

HINT: La soluzione si trova in
http://www.html.it/pag/15617/lavorare-con-i-files/
http://www.html.it/pag/40148/cicli-e-istruzioni-condizionali/
"""

f = open ('file/ex-2.4.txt', 'w') 
while True:
    nn = input("inserisci il tuo nome: ")
    if nn == '':
        break

    dd = int(input("Il giorno in cui sei nato: "))
    mm = input("Il mese in cui sei nato: ")
    aa = int(input("L'anno in cui sei nato: "))

    data = (dd, mm, aa)
    persona = {"Nome": nn, 'Data': data}

    f.write(persona.get("Nome")+" ")
    f.write(str(persona.get('Data')[0])+" ")
    f.write(persona.get('Data')[1]+" ")
    f.write(str(persona.get('Data')[2])+"\n")

f.close()


