# https://leetcode.com/problems/kth-largest-element-in-an-array/

from typing import List
import unittest
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return findKthLargest(nums, k)


def findKthLargest(nums, k):
    nlargest = heapq.nlargest(k, nums) # O(n)
    return nlargest[-1]


class MyTest(unittest.TestCase):
    def test_1(self):
        nums = [3,2,1,5,6,4]
        k = 2
        received = findKthLargest(nums, k)
        expected = 5
        self.assertEqual(received, expected)

    def test_2(self):
        nums = [3,2,3,1,2,4,5,5,6]
        k = 4
        received = findKthLargest(nums, k)
        expected = 4
        self.assertEqual(received, expected)


if __name__ == "__main__":
    unittest.main()
