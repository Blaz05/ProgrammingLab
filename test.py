from Esercitazione1 import MovingAverage
from unittest import TestCase

class Test(TestCase):
    def setUp(self):
        self.MovingAverage = MovingAverage(2)
    
    def test_media(self):
        self.assertEqual(self.MovingAverage.compute([2,4]), 3.0)