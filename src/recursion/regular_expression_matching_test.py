# https://leetcode.com/problems/regular-expression-matching/

import unittest

# TODO: This does not pass all tests
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == "":
            return s == ""

        if s == "":
            if p == "":
                return True
            elif self.isStarred(p):
                return self.isMatch(s, p[2:])
            else:
                return False

        if not self.isStarred(p):
            if self.isCharacterMatch(s[0], p[0]):
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        else:
            # * = 0
            if not self.isCharacterMatch(s[0], p[0]):
                return self.isMatch(s, p[2:])
            # * = 1 or more; try every combination
            else:
                i = 1
                while i <= len(s) and self.isCharacterMatch(s[i - 1], p[0]):
                    if self.isMatch(s[i:], p[2:]):
                        return True
                    i += 1
                return False

    def isCharacterMatch(self, a, b):
        assert len(a) == len(b) == 1
        if a == b or b == ".":
            return True
        return False

    def isStarred(self, a):
        if len(a) > 1 and a[1] == "*":
            return True
        return False


class MyTest(unittest.TestCase):
    def setUp(self):
        self.isMatch = Solution().isMatch

    def test_normal_true(self):
        s = "ab"
        p = "ab"
        received = self.isMatch(s, p)
        expected = True
        self.assertEqual(received, expected)

    def test_normal_false(self):
        s = "ab"
        p = "a"
        received = self.isMatch(s, p)
        expected = False
        self.assertEqual(received, expected)

    def test_dot_true(self):
        s = "ab"
        p = "a."
        received = self.isMatch(s, p)
        expected = True
        self.assertEqual(received, expected)

    def test_dot_false(self):
        s = "abc"
        p = "a."
        received = self.isMatch(s, p)
        expected = False
        self.assertEqual(received, expected)

    def test_star_empty_true(self):
        s = ""
        p = "a*"
        received = self.isMatch(s, p)
        expected = True
        self.assertEqual(received, expected)

    def test_star_one_true(self):
        s = "a"
        p = "a*"
        received = self.isMatch(s, p)
        expected = True
        self.assertEqual(received, expected)

    def test_star_multiple_true(self):
        s = "aa"
        p = "a*"
        received = self.isMatch(s, p)
        expected = True
        self.assertEqual(received, expected)

    def test_star_false(self):
        s = "ab"
        p = "a*"
        received = self.isMatch(s, p)
        expected = False
        self.assertEqual(received, expected)

    def test_dot_star(self):
        s = "ab"
        p = ".*"
        received = self.isMatch(s, p)
        expected = True
        self.assertEqual(received, expected)

    def test_dot_star_false(self):
        s = "ab"
        p = ".*c"
        received = self.isMatch(s, p)
        expected = False
        self.assertEqual(received, expected)


if __name__ == "__main__":
    unittest.main()
