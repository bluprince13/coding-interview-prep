import numpy as np
import unittest


def generalizedGCD(num, arr):
    common_factors = find_common_factors(arr)
    gcd =  max(common_factors)
    return gcd

def find_common_factors(arr):
    current_factors = find_factors(arr[0])
    for number in arr[1:]: 
        individual_factors = find_factors(number)
        new_factors = []
        for factor in current_factors:
            if factor in individual_factors:
                new_factors.append(factor)
        current_factors = new_factors 
    return new_factors

def find_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors


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
