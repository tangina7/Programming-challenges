import unittest

from SCRAPING_SINGLES import *

class testMystr(unittest.TestCase):

    def test_read_web(self):
        self.assertIsNotNone("https://www.officialcharts.com/charts/singles-chart/")



if __name__ == "__main__":
    unittest.main()
