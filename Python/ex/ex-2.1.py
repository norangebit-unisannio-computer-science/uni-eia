# EIA 2018 - ESERCIZIO 2.1
"""
Scrivere un programma che consenta di inserire nome (nn), giorno (dd), mese (mm) e anno (aa) di nascita, e utilizzando l'operatore % stampi a video la conca delle stringhe: 

     "Ciao %s."
     "Sei nato il %d-%s-%d."

Il nome dell'utente deve essere mascherato, mostrando solo l'iniziale.
Inserito il nome completo del mese, di questo utilizzare solo i primi 3 caratteri maiuscoli.
Stampare poi la lunghezza del messaggio.

Esempio:
Inserisci il tuo nome: Stefano
Il giorno in cui sei nato: 10
Il mese: Agosto
L'anno: 1994

Ciao S######. Sei nato il 10-AGO-1994.
Messaggio lungo 38 caratteri.

Suggerimento: La soluzione si trova in http://www.html.it/pag/39746/stringhe-in-python/
"""
nn = input("inserisci il tuo nome: ")
dd = int(input("Il giorno in cui sei nato: "))
mm = input("Il mese in cui sei nato: ")
aa = int(input("L'anno in cui sei nato: "))

nn = nn[0]+ '#'*(len(nn)-1)
mm = mm[:3].upper()

s = "Ciao %s. Sei nato il %d-%s-%d."
s1 = "Messaggio lungo %d caratteri."
s=s%(nn, dd, mm, aa)

print(s)
print(s1%(len(s)))