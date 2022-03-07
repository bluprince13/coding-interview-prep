# https://leetcode.com/problems/subsets/


import unittest


def permute(nums):
    # Base condition
    if len(nums) == 1:
        return [nums.copy()]

    result = []
    # e,g. [1, 2, 3]
    for _ in enumerate(nums):
        n = nums.pop(0) # n = 1 on first iteration
        perms = permute(nums) # permute([2, 3]) => [[2, 3], [3, 2]]
        for perm in perms:
            perm.append(n)  # [[2, 3], [3, 2]] => [[2, 3, 1], [3, 2, 1]]
        result.extend(perms)
        nums.append(n) # [2, 3] => [2, 3, 1], so next time we'd pop 2, and permutate [3, 1]
    return result


class Solution:
    def permute(self, nums):
        return permute(nums)


class MyTest(unittest.TestCase):
    def test_0(self):
        nums = [1, 2, 3]
        received = sorted(permute(nums))
        expected = sorted(
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        )
        self.assertEqual(received, expected)

    def test_1(self):
        nums = [0, 1]
        received = sorted(permute(nums))
        expected = sorted([[0, 1], [1, 0]])
        self.assertEqual(received, expected)

    def test_2(self):
        nums = [1]
        received = permute(nums)
        expected = [[1]]
        self.assertEqual(received, expected)


if __name__ == "__main__":
    unittest.main()
