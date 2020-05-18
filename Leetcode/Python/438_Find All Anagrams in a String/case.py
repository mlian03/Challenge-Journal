from solution import Solution
import unittest

def solve(x: str, y: str):
    return Solution().findAnagrams(x, y)

class UnitTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(solve("cbaebabacd", "abc"), [0,6])

    def test_case_2(self):
        self.assertEqual(solve("abab", "ab"), [0, 1, 2])

if __name__ == '__main__':
    unittest.main()
