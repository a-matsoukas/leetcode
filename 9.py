"""
9. Palindrome Number (E)

Given an integer x, return true if x is a palindrome, and false otherwise.


Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.


Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.


Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

    -231 <= x <= 231 - 1

 
Follow up: Could you solve it without converting the integer to a string?
"""


import unittest


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        div = 1
        while div * 10 <= x:
            div *= 10

        while x > 0:
            if x % 10 != x // div:
                return False

            x = (x % div) // 10
            div /= 100

        return True


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.isPal = Solution().isPalindrome

    def test_1(self):
        self.assertTrue(self.isPal(0))

    def test_2(self):
        self.assertTrue(self.isPal(5))

    def test_3(self):
        self.assertTrue(self.isPal(101))

    def test_4(self):
        self.assertTrue(self.isPal(1145411))

    def test_5(self):
        self.assertTrue(self.isPal(90054345009))

    def test_6(self):
        self.assertFalse(self.isPal(-1))

    def test_7(self):
        self.assertFalse(self.isPal(-343))

    def test_8(self):
        self.assertFalse(self.isPal(10))

    def test_9(self):
        self.assertFalse(self.isPal(56432465))

    def test_10(self):
        self.assertFalse(self.isPal(8181))

    def test_11(self):
        self.assertFalse(self.isPal(1000021))


if __name__ == "__main__":
    unittest.main()
