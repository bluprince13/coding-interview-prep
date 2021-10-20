# https://www.hackerrank.com/challenges/max-array-sum

import unittest

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    # Build an output_array of the maxSubsetSum upto the ith element of arr
    output_array = []

    for index_i, i in enumerate(arr):
        if index_i == 0:
            output = max(0, i)
        elif index_i == 1:
            output = max(output_array[-1], i)
        else:
            # maxSubsetSum at i will be the max of the following three choices:
            #   the previous maxSubsetSum
            #   the new number at i (which could be greater than the previous maxSubsetSum, but cannot  be added to it)
            #   the sum of the new number at i and the maxSubsetSum at i-1
            output = max(output_array[-1], i, output_array[-2] + i)
        output_array.append(output)
    return output_array[-1]


class MyTest(unittest.TestCase):
    def test_1(self):
        arr = [-2, 1, 3, -4, 5]

        # -2, 1, 3, 3, 8
        # Postion 2: max(1,3, 1) = 3
        # Position 3: max(3, -4, -3) = 3
        # Postion 4: max(3, 5, 8) = 8

        received = maxSubsetSum(arr)
        expected = 8
        self.assertEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
