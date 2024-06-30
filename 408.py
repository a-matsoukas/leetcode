"""
408. Valid Word Abbreviation (E)

Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

A string such as"word"contains only the following valid abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

Notice that only the above abbreviations are valid abbreviations of the string"word". Any other string is not a valid abbreviation of"word".

Note:
Assumes contains only lowercase letters and abbr contains only lowercase letters and digits.


Example 1:

Given 
s = "internationalization", 
abbr = "i12iz4n":

Return true.


Example 2:

Given 
s = "apple", 
abbr = "a2e":

Return false.
"""


import unittest


class Solution:
    def validWordAbbreviation(self, s: str, abbr: str) -> bool:
        ptr = 0
        currNum = 0
        for char in abbr:
            if ord(char) >= ord("a") and ord(char) <= ord("z"):
                if currNum > 0:
                    ptr += currNum
                    currNum = 0
                if ptr > len(s) or s[ptr] != char:
                    return False
                ptr += 1
            else:
                currNum = currNum * 10 + int(char)

        ptr += currNum

        return ptr == len(s)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.validAbbr = Solution().validWordAbbreviation

    def test_1(self):
        self.assertTrue(self.validAbbr("internationalization", "i12iz4n"))

    def test_2(self):
        self.assertFalse(self.validAbbr("apple", "a2e"))

    def test_3(self):
        self.assertTrue(self.validAbbr("terminal", "8"))

    def test_4(self):
        self.assertTrue(self.validAbbr("intestinal", "i1t1s1i1a1"))

    def test_5(self):
        self.assertFalse(self.validAbbr("claim", "4im"))

    def test_6(self):
        self.assertFalse(self.validAbbr("stampede", "st10ed1"))

    def test_7(self):
        self.assertTrue(self.validAbbr("stampede", "st3ed1"))


if __name__ == "__main__":
    unittest.main()
