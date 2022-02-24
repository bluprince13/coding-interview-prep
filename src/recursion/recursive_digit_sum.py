# https://www.hackerrank.com/challenges/recursive-digit-sum/problem

import unittest


def superDigit(n, k):
    summation = find_sum(n) * k
    if summation > 9:
        return superDigit(summation, 1)
    else:
        return summation


def find_sum(n):
    n_string = str(n)
    return sum(int(i) for i in n_string)


class MyTest(unittest.TestCase):
    def test_1(self):
        n = 123
        k = 3
        received = superDigit(n, k)
        expected = 9
        self.assertEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
