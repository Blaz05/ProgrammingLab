from parte8 import TrendModel
test_data = [50,52,60]  # Definisco dei dati di test
trend_model = TrendModel()  # Istanzio il modello
if trend_model.window != 3:     # Testo che la lungezza della finestra di default venga settata a 3
    raise Exception('Il modello non ha una finestra di default pari a 3, ma di {}'.format(trend_model.window))
prediction = trend_model.predict(test_data)
  # Testo che il risultato sia corretto
if prediction != 65:
    raise Exception('Il modello sbaglia la previsione: ha dato {} invece di 65'.format(prediction))


# Testo anche che il modello non possa funzionare su dati con un numero di mesi diverso da
# quelli della finestra (3 in questo caso): 
wrong_test_data = [50,52,60,70]
try: 
    trend_model.predict(wrong_test_data)
except ValueError: 
    pass
else:
    raise Exception('Il modello non alza alcuna eccezione se applicato su un numero di mesi ' +
                      'diverso da quelli della finestra')


# Infine testo il modello con una finestra di lunghezza diversa da quella di default di 3 mesi
trend_model = TrendModel(window=4)
  # Testo che la lungezza della finestra sia stata settata a 4
if trend_model.window != 4:
    raise Exception('Il modello non ha settata una finestra pari a 4, ma di {}'.format(trend_model.window))
  # Applico il modello con finestra di 4 mesi
test_data_new = [50,52,60,65]
prediction = trend_model.predict(test_data_new)
  # Testo che il risultato sia corretto
if prediction != 70:
    raise Exception('Il modello sbaglia la previsione: ha dato {} invece di 70'.format(prediction)) 
print('ALL TESTS PASS')