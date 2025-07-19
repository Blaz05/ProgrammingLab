import unittest
from Parte7 import CSVFile, NumericalCSVFile

class TestNome(unittest.TestCase):
    
    def test_get_data_range_valido(self):
        f = CSVFile('shampoo_sales.csv')
        dati = f.get_data(1, 3)
        self.assertIsInstance(dati, list)
        self.assertGreater(len(dati), 0)
