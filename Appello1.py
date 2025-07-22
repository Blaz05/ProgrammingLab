class ExamException(Exception):
    pass

class CSVTimeSeriesFile:
    def  __init__(self, name):
        self.name = name
        try:
            with open(self.name, 'r') as testo:
                pass
        except:
            raise ExamException('Impossibile aprire il file.')

    def get_data(self):
        contenuto = []
        with open(self.name, 'r') as testo:
            try:
                for linea in testo:
                    contenuto.append(linea.strip().split(','))
            except:
                raise ExamException('Impossibile leggere il file.')
        data = contenuto[1:]
        for lista in data:
            try:
                lista[1] = float(lista[1])
            except:
                lista[1] = 'mancante'
        return data

time_series_file = CSVTimeSeriesFile(name='GlobalTemperatures.csv')
time_series = time_series_file.get_data()

def compute_variations(time_series, first_year, last_year, N):
    
    if first_year > last_year:
        raise ExamException("L'anno di partenza non può essere maggiore dell'anno della fine.")
    if N >= last_year-first_year:
        raise ExamException("Il parametro della finestra N deve essere strettamente minore " \
                            "della lunghezza dell’intervallo considerato")

    '''Creo un dizionario con chiave l'anno e il valore associato 
        la lista delle temperature medie mensili'''
    temp_per_anno = {}
    for lista in time_series:
        data = lista[0].strip().split('/')
        anno = int(data[0])
        if anno not in temp_per_anno.keys():
            temp_per_anno[anno] = []
        if lista[1] != 'mancante':
            temp_per_anno[anno].append(lista[1])
    
    
    '''Creo un nuovo dizionario che contiene la media delle temperature annuali per ciascun anno'''
    temp_medie = {}
    for anno in temp_per_anno.keys():
        temp_medie[anno] = sum(temp_per_anno[anno])/len(temp_per_anno[anno])
    
    '''Creo un ulteriore dizionario per calcolare la variazione tra gli anni inseriti'''
    variazioni = {}
    for anno in range(first_year, last_year + 1):
        if anno not in temp_medie:
            continue
        
        # Calcola la media mobile degli N anni precedenti
        medie_prec = []
        for i in range(1, N + 1):
            anno_prec = anno - i
            if anno_prec in temp_medie:
                medie_prec.append(temp_medie[anno_prec])
        
        if len(medie_prec) == N:
            media_mobile = sum(medie_prec) / N
            variazioni[anno] = temp_medie[anno] - media_mobile
    
    return variazioni

print(compute_variations(time_series,1900,1910,3))