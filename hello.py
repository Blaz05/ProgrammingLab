dati = []
with open( 'shampoo_sales.csv' , 'r' ) as mio_file: 
    for linea in mio_file:
        elementi = linea.split(',')
    if elementi[0] != 'Date':
        data = elementi[0]
        valore = float(elementi[1])
        dati.append([data, valore])

print(dati)