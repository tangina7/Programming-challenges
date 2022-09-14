import unittest

from ROD_CONVERSIONS import *

class TestCalc(unittest.TestCase):

    def test_metres(self):
        self.assertEqual(Metres(1),5.0292)

    def test_furlong(self):
        self.assertEqual(Furlongs(10),0.25)

if __name__ == "__main__":
    unittest.main()
