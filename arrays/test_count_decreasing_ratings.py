# Amazon online assessment
# A variation of https://www.geeksforgeeks.org/find-the-count-of-strictly-decreasing-subarrays/

import unittest

# [3]
# 1

# [3 2]
# 2 + 1

# [3 2 1]
# 3 + 2 + 1

# [4 3 2 1]
# 4 + 3 + 2 + 1


def countDecreasingRatings(arr):
    n = len(arr)
    if n == 0:
        return 0
    i, length, count = 1, 1, 0
    while i < n:
        if arr[i] == arr[i - 1] - 1:
            length += 1
        else:
            count += (length * (length + 1)) // 2
            length = 1
        i += 1
    count += (length * (length + 1)) // 2
    return count


class MyTest(unittest.TestCase):
    def test_1(self):
        N = 15
        received = countDecreasingRatings([4, 3, 5, 4, 3])
        expected = 9
        self.assertEqual(received, expected)

    def test_2(self):
        received = countDecreasingRatings([4, 2, 3, 1])
        expected = 4
        self.assertEqual(received, expected)

    def test_3(self):
        received = countDecreasingRatings([])
        expected = 0
        self.assertEqual(received, expected)


if __name__ == "__main__":
    unittest.main()
