nn = input("Inserisci il tuo nome: ")
gg = int (input("Inserisci il giorno di  nascita: "))
mm = input("inserisci il mese di nascita: ")
aa = int(input("Inserisci anno di nascita: "))

out='Ciao %s. Sei nato il %d-%s-%d'
out2 = 'il messaggio lungo %d'

nn = nn[0] + '#'*(len(nn)-1)
mm = mm[0:3].upper()
out=out%(nn, gg, mm, aa)
print(out)
print(out2%(len(out)))


