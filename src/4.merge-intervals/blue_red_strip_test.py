# Google interview 22-03

# You are given a long strip. There are N segments on the strip colored red.
# Other segments are colored blue.
# You are given another blue strip with length L.
# Try to cover the long strip with the new blue strip, so that the total length of visible red is minimised.

# Input: A list of N intervals, an integer L.
# Output: Minimum total length of red left on the blue strip.

# Example
# Input:
#   red_intervals = [[0, 2], [4, 9], [10, 12]]   (Indices 2, 9, 12 are not included)
#   L = 7
# Intepretation:
#   0   1   2   3   4   5   6   7   8   9   10  11  12
#   r   r   b   b   r   r   r   r   r   b   r   r   b
# Solution:
#   The best coverage has 3 reds left.
#   0   1   2   3   4   5   6   7   8   9   10  11  12
#   b   b   b   b   b   b   b   b   r   b   r   r   b

# Approach:
# Repeat for each red interval:
#   1. Place the blue strip at the start of the red interval.
#   2. Find the red interval where the blue strip terminates.
#   3. Calculate the length covered by the blue strip.
# Optimisation:
#   By using start and end pointers (sliding window), we can achieve O(N) time
#   complexity.
#   Otherwise, it'd be O(N^2) as we'd have a loop within a loop.

import unittest


def get_red_strips_left(red_intervals, blue_length):
    N = len(red_intervals)
    max_red_length_covered = 0
    red_length_fully_covered = 0
    start_pointer = 0
    end_pointer = 0
    while start_pointer < N and end_pointer < N:
        current_start_interval = red_intervals[start_pointer]
        current_end_interval = red_intervals[end_pointer]
        blue_start_index = current_start_interval[0]
        # blue_end_index is the index after the blue strip terminates, i.e. non inclusive
        blue_end_index = blue_start_index + blue_length

        # Case A: current interval is fully covered by blue strip
        if blue_end_index >= current_end_interval[1]:
            red_length_fully_covered += (
                current_end_interval[1] - current_end_interval[0]
            )
            red_length_covered = red_length_fully_covered
            end_pointer += 1
        else:
            # Case B: current interval is partially covered by blue strip
            if blue_end_index < current_end_interval[1]:
                red_length_partially_covered = blue_end_index - current_end_interval[0]
                red_length_covered = (
                    red_length_fully_covered + red_length_partially_covered
                )

            # update start_pointer and red_length_fully_covered for next iteration
            red_length_fully_covered -= (
                current_start_interval[1] - current_start_interval[0]
            )
            start_pointer += 1

        #  update max_red_length_covered
        if red_length_covered > max_red_length_covered:
            max_red_length_covered = red_length_covered

    red_length_total = sum(end - start for [start, end] in red_intervals)
    return red_length_total - max_red_length_covered


class MyTest(unittest.TestCase):
    def test_basic(self):
        red_intervals = [[0, 2], [4, 9], [10, 12]]
        blue_length = 7
        received = get_red_strips_left(red_intervals, blue_length)
        expected = 3
        self.assertEqual(received, expected)

    def test_when_blue_strip_larger_than_last_interval(self):
        red_intervals = [[0, 2], [10, 15]]
        blue_length = 7
        received = get_red_strips_left(red_intervals, blue_length)
        expected = 2
        self.assertEqual(received, expected)

    def test_when_blue_strip_smaller_than_last_interval(self):
        red_intervals = [[0, 2], [10, 15]]
        blue_length = 3
        received = get_red_strips_left(red_intervals, blue_length)
        expected = 4
        self.assertEqual(received, expected)


if __name__ == "__main__":
    unittest.main()
