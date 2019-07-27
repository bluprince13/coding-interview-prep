# https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem

import unittest


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


class MyTest(unittest.TestCase):
    def test_1(self):
        n = 3
        received = fibonacci(n)
        expected = 2
        self.assertEqual(received, expected)

    def test_2(self):
        n = 6
        received = fibonacci(n)
        expected = 8
        self.assertEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
