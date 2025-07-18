class ExamException(Exception):
            pass

class CSVTimeSeriesFile:
    def __init__(self, name):
        self.name = name
    
    def get_data(self):
        try:
            with open(self.name, 'r') as testo:
                try:
                    contenuto = []
                    for linea in testo:
                        lista = linea.strip().split(',')
                        contenuto.append(lista)
                except:
                    raise ExamException('Il file non è leggibile')
        except:
            raise FileExistsError('Il file non esiste.')
        for lista in contenuto:
            if lista[0] != 'date':
                try:
                    lista[1] = int(lista[1])
                except:
                    lista[1] = 'Mancante'          
        return contenuto

time_series_file = CSVTimeSeriesFile(name='data.csv') 
time_series = time_series_file.get_data()

def compute_variations(time_series, first_year, last_year):
    
    try:
        first_year = int(first_year)
        last_year = int(last_year)
    except:
        raise ExamException('Impossibile convertire in intero.')
    
    if first_year > last_year:
        raise ValueError("L'anno di partenza non può essere più grande dell'anno finale")
    
    passeggeri_per_anno = {}
    for lista in time_series:
        if lista[0] != 'date':
            data = lista[0].strip().split('-')
            anno = int(data[0])
            if anno not in passeggeri_per_anno.keys():
                passeggeri_per_anno[anno] = []
            if isinstance(lista[1], int):
                passeggeri_per_anno[anno].append(lista[1])
    
    media_passeggeri_per_anno = {}
    for anno in passeggeri_per_anno.keys():
        media_passeggeri_per_anno[anno] = sum(passeggeri_per_anno[anno])/len(passeggeri_per_anno[anno])

    differenze = []
    anno_prev = None
    for anno in media_passeggeri_per_anno.keys():
        if anno_prev != None and anno >= first_year and anno <= last_year:
            diff = media_passeggeri_per_anno[anno]-media_passeggeri_per_anno[anno_prev]
            differenze.append([f'{anno_prev}-{anno}', diff])
        anno_prev = anno
    
    return differenze

print(compute_variations(time_series,1949,1955))



