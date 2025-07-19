from parte8 import TrendModel
  
  # Definisco dei dati di test
test_data = [50,52,60]
  
  # Istanzio il modello
trend_model = TrendModel()
  
  # Applico il modello
prediction = trend_model.predict(test_data)
  
  # Testo che il risultato sia corretto
if prediction != 65:
    raise Exception('Il modello sbaglia la prediction: ha dato {} invece di 65'.format(prediction))

# Testo anche che il modello non possa funzionare 
# su dei dati con un numero di mesi diverso da 3:

wrong_test_data = [50,52,60,70]
try:
    trend_model.predict(wrong_test_data) 
except ValueError:
    pass 
else:
    raise Exception('Il modello non alza alcuna eccezione se applicato su un numero di mesi diverso da 3')
print('ALL TESTS PASS')
