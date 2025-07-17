from Parte7 import CSVFile, NumericalCSVFile
import unittest

class TestNome(unittest.TestCase):
    def setUp(self):
        self.CSVFile = CSVFile('shampoo_sales.csv')
    
    def test_nome(self):
        self.assertEqual(self.CSVFile.nome, 'shampoo_sales.csv')
