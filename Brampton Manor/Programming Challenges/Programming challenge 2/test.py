import unittest

from Richter import *

class TestCalc(unittest.TestCase):

    def test_calc(self):
        self.assertEqual(calc(5.0),1995262314968.8828)

if __name__ == "__main__":
    unittest.main()
