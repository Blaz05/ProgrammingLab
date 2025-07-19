from Parte7 import CSVFile, NumericalCSVFile
import unittest

class TestNumericalCSVFile(unittest.TestCase):

    def test_inheritance(self):
        f = NumericalCSVFile('shampoo_sales.csv')
        self.assertIsInstance(f, CSVFile)

    def test_valori_numerici(self):
        f = NumericalCSVFile('shampoo_sales.csv')
        dati = f.get_data(1, 5)
        for riga in dati:
            self.assertIsInstance(riga[1], float)

    def test_nome_salvato(self):
        f = NumericalCSVFile('test.csv')
        self.assertEqual(f.nome, 'test.csv')
