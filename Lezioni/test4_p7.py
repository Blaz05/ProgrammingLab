import unittest
from Parte7 import CSVFile, NumericalCSVFile

class TestNome(unittest.TestCase):

    def test_get_data_tipo_start_end(self):
        f = CSVFile('shampoo_sales.csv')
        with self.assertRaises(TypeError):
            f.get_data('uno', 3)
        with self.assertRaises(TypeError):
            f.get_data(1, 'tre')

