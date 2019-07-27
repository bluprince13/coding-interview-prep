# https://www.hackerrank.com/challenges/common-child/problem
# https://en.wikipedia.org/wiki/Longest_common_subsequence_problem

import unittest


# TODO: improve performance; not passing tests on hackerrank
def commonChild(s1, s2):
    m = len(s1)
    n = len(s2)
    arr = [[None for i in range(n + 1)] for j in range(m + 1)]

    # recursive function to calculate longest common subsequence
    def lcs(s1, s2, m, n):
        # check if intermediate result already known
        if arr[m][n] is not None:
            return arr[m][n]
        # base case
        if n == 0 or m == 0:
            result = 0
        # case 1: last letters match
        elif s1[m - 1] == s2[n - 1]:
            result = 1 + lcs(s1, s2, m-1, n-1)
        # case 2: last letters don't match
        else:
            temp1 = lcs(s1, s2, m, n-1)
            temp2 = lcs(s1, s2, m-1, n)
            if temp1 > temp2:
                result = temp1
            else:
                result = temp2
        arr[m][n] = result
        return result
    return lcs(s1, s2, m, n)


class MyTest(unittest.TestCase):
    def test_1(self):
        s1 = "HARRY"
        s2 = "SALLY"
        received = commonChild(s1, s2)
        expected = 2
        self.assertEqual(received, expected)

    def test_2(self):
        s1 = "SHINCHAN"
        s2 = "NOHARAAA"
        received = commonChild(s1, s2)
        expected = 3
        self.assertEqual(received, expected)

    def test_3(self):
        s1 = "AABCD"
        s2 = "ABACD"
        received = commonChild(s1, s2)
        expected = 4
        self.assertEqual(received, expected)

    def test_4(self):
        s1 = "ABACD"
        s2 = "AABCD"
        received = commonChild(s1, s2)
        expected = 4
        self.assertEqual(received, expected)

    def test_5(self):
        s1 = "OUDFRMYMAW"
        s2 = "AWHYFCCMQX"
        received = commonChild(s1, s2)
        expected = 2
        self.assertEqual(received, expected)

    def test_6(self):
        # we could miss a longer child if we latch on to a smaller child
        # in the following example, ACDE is the longest child
        # to find it, we'd have to skip over B in s1!
        s1 = "ABCDE"
        s2 = "ACDEB"
        received = commonChild(s1, s2)
        expected = 4
        self.assertEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
