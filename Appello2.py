class ExamException(Exception):
    pass


class CSVTimeSeriesFile:
    """
    Inizializzo la classe e controllo che il file sia apribile e che contenga dati validi
    """
    def __init__(self, name):
        self.name = name
        try:
            with open(self.name, 'r') as testo:
                try:
                    _ = testo.read()
                except:
                   raise ExamException("Errore: il file non contiene dati validi")
        except:
            raise ExamException("Errore: impossibile aprire il file")

    def get_data(self, country):
        """
        Inizializzo una lista vuota, apro il file, leggo riga per riga e le divido in base alla virgola. Poi, se
        la linea contiene il nome della nazione cercata, la aggiungo a 'contenuto'. Controllo che 'contenuto' non
        sia vuoto, perché vorrebbe dire che non c'è la nazione cercata.
        """
        contenuto = []
        with open(self.name, 'r') as testo:
            for riga in testo:
                linea = riga.strip().split(',')
                if linea[2] == country:
                    contenuto.append(linea)
        
        if len(contenuto) == 0:
            raise ExamException("Errore: il nome del paese non è presente nel file")
        
        """
        Inizializzo una lista e ci aggiungo le liste contenenti la data e la temperatura (convertita in 'float')
        """
        contenuto = contenuto[1:]
        dati = []
        for lista in contenuto:
            try:
                dati.append([lista[0], float(lista[1])])
            except:
                pass

        return(dati)


"""Scrivo questa funzione per non scrivere due volte lo stesso codice"""
def media_annuale(ts, first_year, last_year):
    """
    Inizializzo un dizionario vuoto, estraggo dai dati l'anno della misurazione e lo aggiungo al dizionario,
    assegnandogli come valore una lista, in cui andranno tutte le misurazioni di quell'anno
    """
    time_series = {}
    for lista in ts:
        data = lista[0].strip().split('-')
        anno = int(data[0])

        if anno >= first_year and anno <= last_year:
            if anno not in time_series.keys():
                time_series[anno] = []
            if isinstance(lista[1], float): # aggiungo solo le temperature che sono riuscito a convertire in float
                time_series[anno].append(lista[1])
    
    if len(time_series) == 0:
        raise ExamException("Errore: l’intervallo selezionato non contiene valori validi")
    
    """
    Inizializzo un'altra lista che contiene la media delle temperature per ogni anno
    """
    media_ts = {}
    for anno in time_series.keys():
        media_ts[anno] = sum(time_series[anno]) / len(time_series[anno])
    
    return media_ts


def compute_variations(time_series_1, time_series_2, first_year, last_year):
    """
    Provo a convertire gli anni in interi, poi applico la funzione sovrastante a 'time_series_1' e a 'time_series_2'
    in modo da ottenere un dizionario con chiavi gli anni e valori le medie delle temperature per entrambe.
    """
    try:
        first_year = int(first_year)
        last_year = int(last_year)
    except:
        raise ExamException("Errore: l’anno inserito non `e un intero")
    
    ts1 = media_annuale(time_series_1, first_year, last_year)
    ts2 = media_annuale(time_series_2, first_year, last_year)

    """
    Inizializzo il dizionario in cui le chiavi saranno gli anni, mentre i valori le differenze delle 
    medie annuali tra le due time series.
    """
    differenze = {}
    for anno in range(first_year, last_year + 1):
        if anno in ts1.keys() and anno in ts2.keys():
            differenze[anno] = ts2[anno] - ts1[anno]

    return differenze