# https://www.hackerrank.com/challenges/minimum-swaps-2/problem

def minimumSwaps(arr):
    # let's try some examples
    # example 1:
    #   [4, 1, 3, 2]
    #   [2, 1, 3, 4] - 1
    #   [1, 2, 3, 4] - 2
    # example 1: 3 things wrong, required 2 swaps
    # example 2:
    #   [7, 1, 3, 2, 4, 5, 6]
    #   [2, 1, 3, 7, 4, 5, 6] - 1
    #   [1, 2, 3, 7, 4, 5, 6] - 2
    #   [1, 2, 3, 4, 7, 5, 6] - 3
    #   [1, 2, 3, 4, 5, 7, 6] - 4
    #   [1, 2, 3, 4, 5, 6, 7] - 5
    # example 2: 6 things wrong, required 5 swaps
    # example 4:
    #   [4, 3, 2, 1]
    #   [1, 3, 2, 4] - 1
    #   [1, 2, 3, 4] - 1
    # example 4: 4 things wrong, required 2 swaps
    # if a swap corrects 2 items in one go, then you only need 1 swap for them
    # we have to avoid double accounting in such cases

    length = len(arr)
    i = 0
    result = 0
    # go through each item in array
    while i < length: 
        # if the item is not in the right place
        while arr[i] != i + 1: 
            # make a swap
            arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1] 
            result += 1 
            # check if the new item is in the right place ...
        i += 1
    return result

import unittest

class MyTest(unittest.TestCase):
    def test_1(self):
        arr = [2, 3, 4, 1, 5]
        expected = 3
        received = minimumSwaps(arr)
        self.assertEqual(received, expected)

    def test_2(self):
        arr = [1, 3, 5, 2, 4, 6, 7]
        expected = 3
        received = minimumSwaps(arr)
        self.assertEqual(received, expected)

    def test_3(self):
        arr = [4, 3, 2, 1]
        expected = 2
        received = minimumSwaps(arr)
        self.assertEqual(received, expected)

    def test_4(self):
        arr = [4, 3, 5, 1, 2]
        expected = 3
        received = minimumSwaps(arr)
        self.assertEqual(received, expected)      

if __name__ == '__main__':
    unittest.main()