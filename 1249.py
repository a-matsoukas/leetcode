"""
1249. Minimum Remove to Make Valid Parentheses (M)

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses
( '(' or ')', in any positions ) so that the resulting parentheses string is
valid and return any valid string.

Formally, a parentheses string is valid if and only if:

    It is the empty string, contains only lowercase characters, or
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.

 
Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.


Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

 
Constraints:

    1 <= s.length <= 105
    s[i] is either '(' , ')', or lowercase English letter.
"""


import unittest
from typing import List


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        unmatched = 0
        chars = []

        for c in s:
            if c != ")":
                chars.append(c)
                if c == "(":
                    unmatched += 1
            elif unmatched > 0:
                chars.append(c)
                unmatched -= 1

        filteredChars = []
        for c in chars[::-1]:
            if c == "(" and unmatched > 0:
                unmatched -= 1
            else:
                filteredChars.append(c)

        return "".join(filteredChars[::-1])


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.minRem = Solution().minRemoveToMakeValid

    def test_1(self):
        self.assertEqual(self.minRem(""), "")

    def test_2(self):
        self.assertEqual(self.minRem("lee(t(c)o)de)"), "lee(t(c)o)de")

    def test_3(self):
        self.assertEqual(self.minRem("a)b(c)d"), "ab(c)d")

    def test_4(self):
        self.assertEqual(self.minRem("))(("), "")

    def test_5(self):
        self.assertEqual(self.minRem("(abc((d)efglksj)()"),
                         "(abc((d)efglksj))")

    def test_6(self):
        self.assertEqual(self.minRem("((((()))))"), "((((()))))")

    def test_7(self):
        self.assertEqual(self.minRem("())()((("), "()()")


if __name__ == "__main__":
    unittest.main()
