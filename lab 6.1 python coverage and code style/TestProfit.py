import unittest
import Profit


class ConverterTest(unittest.TestCase):
    def testDictionary(self):              
        expected = -15
        path = "./ProfitDictionary2.txt"
        f = open(path, "a")
        f.write('profit({"cost_price": 2,"sell_price": -1,"inventory": 5}) ")')
        f.close()
        self.assertEquals(Profit.calculateProfit(path),expected)


if __name__ == "__main__":
    unittest.main()
