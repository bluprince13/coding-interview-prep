# no link available
# find the Greatest Common Divisor [GCD] of a list of numbers
import unittest


def generalizedGCD(num, arr):
    arr = sorted(arr)
    gcd = find_gcd(arr[0], arr[1])
    for i in arr[2:]:
        gcd = find_gcd(gcd, i)
    return gcd


def find_gcd(x, y):
    # Euclidean algorithm
    # https://www.hackerrank.com/challenges/functional-programming-warmups-in-recursion---gcd/problem?h_r=internal-search
    while(y):
        x, y = y, x % y
    return x


class MyTest(unittest.TestCase):
    def test_1(self):
        num = 5
        arr = [2, 3, 4, 5, 6]
        received = generalizedGCD(num, arr)
        expected = 1
        self.assertEqual(received, expected)

    def test_2(self):
        num = 5
        arr = [2, 4, 6, 8, 10]
        received = generalizedGCD(num, arr)
        expected = 2
        self.assertEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
