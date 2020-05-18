from solution import Solution
import unittest

def solve(x: str, y: str):
    return Solution().checkInclusion(x, y)

class UnitTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(solve("ab", "eidbaooo"), True)

    def test_case_2(self):
        self.assertEqual(solve("ab", "aeidboaoob"), False)

if __name__ == '__main__':
    unittest.main()
