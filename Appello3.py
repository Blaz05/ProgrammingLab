class ExamException(Exception):
    pass

class CSVTimeSeriesFile:
    def __init__(self, name):
        self.name = name

    def get_data(self, nome):
        contenuto = []
        try:
            testo = open(self.name, 'r')
        except:
            raise ExamException('Impossibile aprire il file.')
        for linea in testo:
            if nome in linea:
                contenuto.append(linea.strip().split(','))
        testo.close()
        if len(contenuto) == 0:
            raise ExamException("Errore: il nome della città non è presente nel file")
        data_temp = []
        for lista in contenuto:
            try:
                data_temp.append([lista[0], float(lista[1])])
            except:
                data_temp.append([lista[0], 'mancante'])
        return data_temp

time_series_file = CSVTimeSeriesFile(name="GlobalLandTemperaturesByMajorCity.csv")
time_series_italy = time_series_file.get_data("Rome")

def compute_slope(time_series, first_year, last_year):
    
    try:
        first_year = int(first_year)
        last_year = int(last_year)
    except:
        raise ExamException("Inserire valori validi")
    
    if first_year > last_year:
        raise ExamException("Il primo anno dev'essere minore dell'anno finale")


    temp_per_anno = {}
    for anno, temp in time_series:
        if anno >= first_year and anno <= last_year:
            if anno not in temp_per_anno:
                temp_per_anno[anno] =[]
            temp_per_anno[anno].append(temp)
    
    temp_per_anno_clean = {}
    for anno in temp_per_anno.keys():
        if len(temp_per_anno[anno]) >= 6:
            temp_per_anno_clean[anno] = temp_per_anno[anno]
    
    for anno in temp_per_anno_clean.keys():
        temp_per_anno_clean[anno] = sum(temp_per_anno_clean[anno])/len(temp_per_anno_clean[anno])
    
    # calcolo le sommatorie
    xi = sorted(temp_per_anno_clean.keys())
    yi = [temp_per_anno_clean[year] for year in xi]

    n = len(xi)
    x_mean = sum(xi) / n
    y_mean = sum(yi) / n

    # calcolo di m
    numeratore = sum((x - x_mean) * (y - y_mean) for x, y in zip(xi, yi))
    denominatore = sum((x - x_mean) ** 2 for x in xi)

    if denominatore == 0:
        raise ExamException ("Il denominatore è pari a 0")
    
    m = numeratore / denominatore
    return m

print(compute_slope(0,1743, 1760))
