from solution import Solution
import unittest

def solve(x: [int]):
    return Solution().maxSubarraySumCircular(x)

class UnitTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(solve([1, -2, 3, -2]), 3)

    def test_case_2(self):
        self.assertEqual(solve([5, -3, 5]), 10)

    def test_case_3(self):
        self.assertEqual(solve([3, -1, 2, -1]), 4)

    def test_case_4(self):
        self.assertEqual(solve([3, -2, 2, -3]), 3)

    def test_case_5(self):
        self.assertEqual(solve([-2, -3, -1]), -1)

if __name__ == '__main__':
    unittest.main()
