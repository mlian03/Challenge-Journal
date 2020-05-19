from solution import StockSpanner
import unittest

def solve(prices: [[int]]):
    obj = StockSpanner()
    spans = []
    for price in prices:
        spans.append(obj.next(price[0]))
    return spans

class UnitTest(unittest.TestCase):
    def test_case(self):
        self.assertEqual(solve(
            [[100],[80],[60],[70],[60],[75],[85]]
        ), [1,1,1,2,1,4,6])

if __name__ == '__main__':
    unittest.main()
