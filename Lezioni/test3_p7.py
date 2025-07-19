import unittest
from Parte7 import CSVFile, NumericalCSVFile

class TestNome(unittest.TestCase):

    def test_get_data_range_non_valido(self):
        f = CSVFile('shampoo_sales.csv')
        with self.assertRaises(ValueError):
            f.get_data(5, 2)

