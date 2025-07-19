import unittest
from Parte7 import CSVFile, NumericalCSVFile

class TestCSVFile(unittest.TestCase):

    def test_nome_file(self):
        f = CSVFile('test.csv')
        self.assertEqual(f.nome, 'test.csv')

    def test_nome_non_stringa(self):
        with self.assertRaises(TypeError):
            CSVFile(123)

    def test_get_data_range_valido(self):
        f = CSVFile('shampoo_sales.csv')
        dati = f.get_data(1, 3)
        self.assertIsInstance(dati, list)
        self.assertGreater(len(dati), 0)

    def test_get_data_range_non_valido(self):
        f = CSVFile('shampoo_sales.csv')
        with self.assertRaises(ValueError):
            f.get_data(5, 2)

    def test_get_data_tipo_start_end(self):
        f = CSVFile('shampoo_sales.csv')
        with self.assertRaises(TypeError):
            f.get_data('uno', 3)
        with self.assertRaises(TypeError):
            f.get_data(1, 'tre')


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


if __name__ == '__main__':
    unittest.main()
