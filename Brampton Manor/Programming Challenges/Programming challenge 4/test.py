import unittest

from WIND_CHILL import *

class TestCalc(unittest.TestCase):

    def test_values(self):
        self.assertEqual(values(10,15),-6.5895344209562525)


if __name__ == "__main__":
    unittest.main()
