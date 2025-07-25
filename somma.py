from unittest import TestCase
from prove import TrendModel

class Test(TestCase):
    def setUp(self):
        self.TrendModel = TrendModel(3)

    def test_verifica(self):
        data = [50,52,60]
        self.assertEqual(self.TrendModel.predict(data), 65)
    
    def test_verifica_4(self):
        data = [50,52,60]
        self.assertEqual(self.TrendModel.window, len(data))

    def test_numeri_interi(self):
        data = [50,52,60]
        self.assertNotIsInstance(self.TrendModel.predict(data), str)