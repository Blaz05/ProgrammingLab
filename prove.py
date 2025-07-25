class ExamException():
    pass

class CSVTimeSeriesFile:
    def __init__(self,name):
        self.name = name
    
    def get_data(self):
        contenuto = []
        with open(self.name, 'r') as testo:
            for riga in testo:
                contenuto.append(riga.strip().split(','))
        for lista in contenuto:
            if lista[1] != 'LandAverageTemperature':
                lista[1] = float(lista[1])
        return contenuto
    
time_series_file = CSVTimeSeriesFile(name='GlobalTemperatures.csv')
time_series = time_series_file.get_data()

def compute_variations(time_series, first_year, last_year, N):
    temp_per_anno = {}
    for lista in time_series:
        if lista[0] != 'dt':    
            data = lista[0].strip().split('/')
            anno = int(data[0])

            if anno not in temp_per_anno.keys():
                temp_per_anno[anno] = []
            if isinstance(lista[1], float):
                temp_per_anno[anno].append(lista[1])
    
    media_annuale = {}
    for anno in temp_per_anno.keys():
        if len(temp_per_anno[anno]) != 0:
            media_annuale[anno] = sum(temp_per_anno[anno]) / len(temp_per_anno[anno])

    diff = {}
    for year in range(first_year, last_year+1):
        anni = []
        for i in range(1,N+1):
            anno_prec = year - i    
            if anno_prec not in media_annuale.keys():
                continue
            anni.append(media_annuale[anno_prec])
        if len(anni) == N:
            media_mobile = sum(anni) / N
            diff[year] = media_annuale[year] - media_mobile
        else:
            continue

    return diff

print(compute_variations(time_series, 1900,1910,3))