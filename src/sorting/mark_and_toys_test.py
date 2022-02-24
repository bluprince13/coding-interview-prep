# https://www.hackerrank.com/challenges/mark-and-toys/problem

import unittest


def maximumToys(prices, k):
    prices = sorted(prices)
    total = 0
    for number, price in enumerate(prices):
        total += price
        if total > k:
            return number
    return len(prices)


class MyTest(unittest.TestCase):
    def test_1(self):
        k = 50
        prices = [1, 12, 5, 111, 200, 1000, 10]
        received = maximumToys(prices, k)
        expected = 4
        self.assertEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
