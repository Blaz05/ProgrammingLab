class ExamException(Exception):
    pass

class CSVTimeSeriesFile:
    def __init__(self, name):
        self.name = name
        try:
            with open('GlobalTemperatures.csv', 'r') as testo:
                pass
        except:
            raise ExamException('Errore: impossibile aprire il file.')
    
    def get_data(self):
        contenuto = []
        with open('GlobalTemperatures.csv', 'r') as testo:
            for linea in testo:
                contenuto.append(linea.split(','))
            for lista in contenuto:
                if lista[0] != 'dt':
                    try:
                        lista[1] = float(lista[1])
                    except Exception as e:
                        print("Errore: {}".format(e))
        return contenuto

file_name = CSVTimeSeriesFile(name='GlobalTemperatures.csv')
time_series = file_name.get_data()

def compute_variations(time_series, first_year, last_year, N):
    
    if first_year-N < 1900:
        raise Exception('Il primo anno inserito sfora il limite temporale')
    
    if last_year-first_year <= N:
        raise ExamException('Il parametro della finestra N deve essere strettamente minore della ' \
                            'lunghezza dell’intervallo considerato.')

    diz = {}
    for lista in time_series:
        if lista[0] != 'dt':
            data = lista[0].split('/')
            data[0] = int(data[0])
            if data[0] not in diz.keys():
                diz[data[0]] = []
            diz[data[0]].append(lista[1])
    
    media = []
    for lista in diz.values():
        media.append(sum(lista)/len(lista))

    medie_annuali = {}
    i = 0
    for anno in diz.keys():
        medie_annuali[anno] = (media[i])
        i += 1
    return medie_annuali
    

print(compute_variations(time_series,1910,1914,5))










        