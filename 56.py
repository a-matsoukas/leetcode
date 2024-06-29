"""
56. Merge Intervals (M)

Given an array of intervals where intervals[i] = [starti, endi], merge all
overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.

 
Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].


Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

    1 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 104
"""


import unittest
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []

        for s, e in intervals:
            if not res or res[-1][1] < s:
                res.append([s, e])
            elif res[-1][1] >= s and res[-1][1] < e:
                res[-1][1] = e

        return res


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.merge = Solution().merge

    def test_1(self):
        self.assertEqual(self.merge([[1, 3], [2, 6], [8, 10], [15, 18]]), [
                         [1, 6], [8, 10], [15, 18]])

    def test_2(self):
        self.assertEqual(self.merge([[1, 4], [4, 5]]), [[1, 5]])

    def test_3(self):
        self.assertEqual(self.merge([]), [])

    def test_4(self):
        self.assertEqual(self.merge([[4, 10], [1, 3], [2, 4]]), [[1, 10]])

    def test_5(self):
        self.assertEqual(self.merge([[0, 1], [1, 1]]), [[0, 1]])

    def test_6(self):
        self.assertEqual(self.merge([[9, 10], [7, 8], [1, 3], [4, 6]]), [
                         [1, 3], [4, 6], [7, 8], [9, 10]])


if __name__ == "__main__":
    unittest.main()
