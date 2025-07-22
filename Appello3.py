class ExamException(Exception):
    pass

class CSVTimeSeriesFile:
    def __init__(self, name):
        self.name = name
    
    def get_data(self, city):
        contenuto = []
        try:
            with open(self.name, 'r') as testo:
                for linea in testo:
                    linea = linea.strip().split(',')
                    if linea[3] == city:
                        try:
                            contenuto.append([linea[0], float(linea[1])])
                        except:
                            pass
        except:
            raise ExamException("Impossibile aprire il file.")
        if len(contenuto) == 0:
            raise ExamException("La città non è presente nel file.")

        return contenuto
    
time_series_file = CSVTimeSeriesFile(name="GlobalLandTemperaturesByMajorCity.csv")
time_series_italy = time_series_file.get_data(city="Rome")


def compute_slope(time_series_italy, first_year, last_year):
    """
    Controllo che first_year e last_year siano interi e controllo che il primo sia minore dell'altro
    """
    if not isinstance(first_year, int) or not isinstance(last_year, int):
        raise ExamException("Il primo anno e quello finale devono essere numeri interi")
    if first_year > last_year:
        raise ExamException("Il primo anno non può essere maggiore dell'ultimo.")
    
    """
    Creo una lista vuota, per ogni lista nella lista time_series_italy, estraggo la data, da data estraggo l'anno
    e lo converto in intero. Poi, se l'anno sta nell'intervallo di anni dato, lo aggiungo al dizionario e ci associo
    una lista vuota. Nella lista andranno tutte le temprerature di quell'anno.
    """
    temp_per_anno = {}
    for lista in time_series_italy:
        data = lista[0].split('-')
        anno = int(data[0])
        
        if anno >= first_year and anno <= last_year:
            if anno not in temp_per_anno.keys():
                temp_per_anno[anno] = []
            temp_per_anno[anno].append(lista[1])
    
    """
    Creo una nuova lista che contiene solamente gli anni per i quali abbiamo 6 osservazioni o più.
    """
    temp_per_anno_clean = {}
    for anno in temp_per_anno.keys():
        if len(temp_per_anno[anno]) >= 6:
            temp_per_anno_clean[anno] = temp_per_anno[anno]
    
    """
    Creo una nuova lista in cui a ogni anno è associata la media delle temperature per quell'anno
    """
    medie_per_anno = {}
    for anno in temp_per_anno_clean:
        medie_per_anno[anno] = sum(temp_per_anno_clean[anno]) / len(temp_per_anno_clean[anno])
    
    """
    Calcolo la media di tutti gli anni dati in input, e il valore medio delle temperature medie annuali
    """
    media_anni = []
    media_temp_anni = []
    for anni in range(first_year, last_year+1):
        if anni in medie_per_anno.keys():    
            media_anni.append(anni)
            media_temp_anni.append(medie_per_anno[anni])

    if len(media_anni) == 0:
        raise ExamException("Impossibile dividere per 0")

    # calcolo le sommatorie
    x = sum(media_anni) / len(media_anni)
    y = sum(media_temp_anni) / len(media_temp_anni)
    
    # calcolo di m
    numeratore = 0
    for i in range(len(media_anni)):
        numeratore += (media_anni[i]-x)*(media_temp_anni[i]-y)
    
    denominatore = 0
    for i in range(len(media_anni)):
        denominatore += (media_anni[i]-x)**2

    if denominatore == 0:
        raise ExamException("Il denominatore non può essere uguale a 0")
    
    m = numeratore / denominatore
    return ([x,y,m])

print(compute_slope(time_series_italy, 1743, 1900))