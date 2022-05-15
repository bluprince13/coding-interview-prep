# https://leetcode.com/problems/merge-intervals/

from typing import List
import unittest


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        return merge(intervals)


def merge(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])

    merged_intervals = []
    for interval in intervals:
        if not merged_intervals:
            merged_intervals.append(interval)
        else:
            last_interval = merged_intervals[-1]
            if last_interval[1] >= interval[0]:
                merged_intervals[-1] = [
                    last_interval[0],
                    max(last_interval[1], interval[1]),
                ]
            else:
                merged_intervals.append(interval)
    return merged_intervals


class MyTest(unittest.TestCase):
    def test_1(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        received = merge(intervals)
        expected = [[1, 6], [8, 10], [15, 18]]
        self.assertEqual(received, expected)

    def test_2(self):
        intervals = [[1, 4], [4, 5]]
        received = merge(intervals)
        expected = [[1, 5]]
        self.assertEqual(received, expected)


if __name__ == "__main__":
    unittest.main()
