class ExamException(Exception):
            pass

class CSVTimeSeriesFile:
    def __init__(self, nome):
        self.name = nome
    
    def get_data(self):
        contenuto = []
        try:
            with open(self.name, 'r') as testo:
                for linea in testo:
                    elementi = linea.split(',')
                    if elementi[0] != 'date':
                        try:
                            elementi[1] = int(elementi[1])
                        except:
                            elementi[1] = 0
                    contenuto.append(elementi)
        except Exception as e:
            print(f"Impossibile aprire il file. Errore: {e}")
        return contenuto[1:]
    

time_series_file = CSVTimeSeriesFile('data.csv')
time_series = time_series_file.get_data()


def compute_variations(time_series, first_year, last_year):
    try:
        first_year = int(first_year)
        last_year = int(last_year)
    except Exception as error:
        print(f"Inserire valore valido. Errore: {error}")

    diz_passeggeri = {}
    for lista in time_series:
        data = lista[0].split('-')
        anno = int(data[0])
        if anno >=first_year and anno <= last_year:
            if anno not in diz_passeggeri.keys():
                diz_passeggeri[anno] = []
            diz_passeggeri[anno].append(lista[1])

    medie_annuali = []
    for anno in sorted(diz_passeggeri.keys()):
        somma = sum(diz_passeggeri[anno])
        lunghezza =  len(diz_passeggeri[anno])
        media = somma/lunghezza

    dizionario_variazioni = {}
    for i in range(len(medie_annuali) - 1):
        # medie_annuali[i] = [anno_i, media_i]
        # medie_annuali[i+1] = [anno_{i+1}, media_{i+1}]

        # Chiave = "anno_i-anno_{i+1}" 
        chiave = str(medie_annuali[i][0]) + '-' + str(medie_annuali[i+1][0])
        # Valore = media_{i+1} - media_i
        valore = medie_annuali[i+1][1]-medie_annuali[i][1]
        dizionario_variazioni[chiave] = valore
    return dizionario_variazioni

print(compute_variations(time_series,1950,1960))

