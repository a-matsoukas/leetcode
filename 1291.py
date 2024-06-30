"""
1291. Sequential Digits (M)

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 
Example 1:

Input: low = 100, high = 300
Output: [123,234]


Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
 

Constraints:

    10 <= low <= high <= 10^9
"""

import unittest
from typing import List
from collections import deque


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # res = []

        # lowDigs = len(str(low))
        # highDigs = len(str(high))

        # for numDigs in range(lowDigs, highDigs + 1):

        #     for startNum in range(1, 9 - numDigs + 2):

        #         num = 0
        #         for i in range(startNum, startNum + numDigs):
        #             num = num * 10 + i

        #         if num >= low:
        #             if num <= high:
        #                 res.append(num)
        #             else:
        #                 return res

        # return res

        res = []
        queue = deque(range(1, 10))

        while queue:
            currNum = queue.popleft()

            if currNum >= low and currNum <= high:
                res.append(currNum)

            lastDig = currNum % 10
            if lastDig < 9:
                nextNum = currNum * 10 + lastDig + 1

                if nextNum <= high:
                    queue.append(nextNum)
        return res


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.seqDig = Solution().sequentialDigits

    def test_1(self):
        self.assertListEqual(self.seqDig(100, 300), [123, 234])

    def test_2(self):
        self.assertListEqual(self.seqDig(1000, 13000), [
                             1234, 2345, 3456, 4567, 5678, 6789, 12345])

    def test_3(self):
        self.assertListEqual(self.seqDig(58, 155), [67, 78, 89, 123])

    def test_4(self):
        self.assertListEqual(self.seqDig(67, 67), [67])


if __name__ == "__main__":
    unittest.main()
