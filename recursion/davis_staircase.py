# https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem

import unittest

store = {}


def stepPerms(n):
    if n in store:
        return store[n]
    if n == 1:
        result = 1
    elif n == 2:
        result = 2
    elif n == 3:
        result = 4
    else:
        result = stepPerms(n - 1) + stepPerms(n - 2) + stepPerms(n - 3)
    store[n] = result
    return result


class MyTest(unittest.TestCase):
    def test_1(self):
        n = 3
        received = stepPerms(n)
        expected = 4
        self.assertEqual(received, expected)

    def test_2(self):
        n = 7
        received = stepPerms(n)
        expected = 44
        self.assertEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
