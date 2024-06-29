"""
49. Group Anagrams (M)

Given an array of strings strs, group the anagrams together. You can return the
answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.

 
Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


Example 2:

Input: strs = [""]
Output: [[""]]


Example 3:

Input: strs = ["a"]
Output: [["a"]]

 
Constraints:

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.
"""


import unittest
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for str in strs:
            groups[tuple(sorted(str))].append(str)

        res = []

        for group in groups:
            res.append(groups[group])

        return res


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.groupAns = Solution().groupAnagrams

    def test_1(self):
        res = self.groupAns(["eat", "tea", "tan", "ate", "nat", "bat"])
        for group in res:
            group.sort()
        exp = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        for group in exp:
            group.sort()
        self.assertCountEqual(res, exp)

    def test_2(self):
        res = self.groupAns([""])
        for group in res:
            group.sort()
        exp = [[""]]
        for group in exp:
            group.sort()
        self.assertCountEqual(res, exp)

    def test_3(self):
        res = self.groupAns(["a"])
        for group in res:
            group.sort()
        exp = [["a"]]
        for group in exp:
            group.sort()
        self.assertCountEqual(res, exp)

    def test_4(self):
        res = self.groupAns(
            ["late", "tale", "tail", "name", "mane", "aa", "aaa", ""])
        for group in res:
            group.sort()
        exp = [["late", "tale"], ["tail"], [
            "name", "mane"], ["aa"], ["aaa"], [""]]
        for group in exp:
            group.sort()
        self.assertCountEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
