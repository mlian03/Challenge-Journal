from ListNode import ListNode
from solution import Solution
import unittest

def solve(x: [int]) -> ListNode:
    head = ListNode.generate(x)
    newHead =  Solution().oddEvenList(head)
    vals = []
    while newHead:
        vals.append(newHead.val)
        newHead = newHead.next
    return vals

class UnitTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(solve([1, 2, 3, 4, 5]), [1, 3, 5, 2, 4])

    def test_case_2(self):
        self.assertEqual(solve([2, 1, 3, 5, 6, 4, 7]), [2, 3, 6, 7, 1, 5, 4])

if __name__ == '__main__':
    unittest.main()
