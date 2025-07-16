# Scrivete un programma che riceva una data di nascita come input e visualizzi l’età 
# dell’utente e il numero di giorni, ore, minuti e secondi che mancano al prossimo compleanno.

import datetime

giorno = input('Inserisci il giorno di nascita: ').strip()
mese = input('Inserisci il mese di nascita: ').strip()
anno = input("Inserisci l'anno di nascita: ").strip()
print("Data di nascita: {}/{}/{}".format(giorno, mese, anno))
try:
    giorno = int(giorno)
    mese = int(mese)
    anno = int(anno)
except Exception as e:
    print("Inserire numeri interi. Errore: {}".format(e))
else:    
    if(0 < giorno <= 31 and 0 < mese <= 12 and 1900 < anno <= 2024):
        now = datetime.datetime.now()
        if(datetime.datetime(2025, mese, giorno, 0,0,0) > now):
            età = 2024 - anno
            print("Età: {}".format(età))
            compleanno = datetime.datetime(2025, mese, giorno, 0,0,0)
            differenza = compleanno - now
        else:
            età = 2025 - anno
            print("Età: {}".format(età))
            compleanno = datetime.datetime(2026, mese, giorno, 0,0,0)
            differenza = compleanno - now
        print("Fino al prossimo compleanno: {}".format(differenza))
    else:
        raise ValueError("Inserire valori reali.")