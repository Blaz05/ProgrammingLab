class CSVFile:
    def __init__(self, nome):
        if not isinstance(nome, str):
            raise TypeError('Il nome deve essere una stringa')
        self.nome = nome
    def get_data(self, start=None, end=None):
        if(start != None and end != None):
            if not isinstance(start, int):
                raise TypeError("L'inizio deve essere un numero intero")
            if not isinstance(end, int):
                raise TypeError("L'inizio deve essere un numero intero")
            if not (start <= end):
                raise ValueError("L'indice della frase iniziale non può essere maggiore dell'indice della frase finale")
        try:
            with open(self.nome, 'r') as testo:
                contenuto=testo.readlines()
        except Exception as e:
            print('Errore: {}'.format(e))
        
        lista = []
        
        for i, linea in enumerate(contenuto):
            if(start != None and end != None):
                if(i >= start and i <= end):
                    valori = linea.strip().split(',')
                    lista.append(valori)
            else:
                if(i != 0):
                    valori = linea.strip().split(',')
                    lista.append(valori)
        return lista

class NumericalCSVFile(CSVFile):
    def __init__(self, nome):
        super().__init__(nome)
    def get_data(self, *args, **kwargs):
        dati = super().get_data(*args, **kwargs)
        nuova_lista = []
        for lista in dati:
            try:
                numero = float(lista[1])
                tmp = [lista[0], numero]
                nuova_lista.append(tmp)
            except Exception as e:
                print('Errore: {}'.format(e))
                continue
        return nuova_lista


dati = CSVFile('shampoo_sales.csv').get_data(1, 7)
print(dati) 

# dati = NumericalCSVFile('shampoo_sales.csv').get_data()
# print(dati)