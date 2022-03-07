# https://leetcode.com/problems/subsets/


import unittest


def find_subsets(nums):
    subsets = [[]]
    for num in nums:
        temp = []
        for subset in subsets:
            temp.append(subset + [num])
        subsets.extend(temp)
    return subsets


class Solution:
    def subsets(self, nums):
        return find_subsets(nums)


class MyTest(unittest.TestCase):
    def test_0(self):
        nums = [0]
        received = find_subsets(nums)
        expected = [[], [0]]
        self.assertEqual(received, expected)

    def test_1(self):
        nums = [1, 2, 3]
        received = find_subsets(nums)
        expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        self.assertEqual(received, expected)


if __name__ == "__main__":
    unittest.main()
