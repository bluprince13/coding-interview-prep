# https://adventofcode.com/2021/day/7

# Example
# data = [0, 1, 4]
# 0: 0                  + 1             + (1 + 2 + 3 + 4)   = 11
# 1: 1                  + 0             + (1 + 2 + 3)       = 7
# 2: (1 + 2)            + 1             + (1 + 2)           = 7
# 3: (1 + 2 + 3)        + (1 + 2)       + 1                 = 10
# 4: (1 + 2 + 3 + 4)    + (1 + 2 + 3)   + 0                 = 11

# n = new_value - old_value     e.g. 4 - 1                  = 3
# cost = n * (n + 1) / 2        e.g. 3 * (3 + 1) / 2        = 6

import unittest
import math
from functools import reduce
import statistics


def parse(lines):
    return list(map(int, lines[0].split(",")))


def get_data(file):
    with open(file) as f:
        lines = f.read().splitlines()
    return parse(lines)


def get_data(file):
    with open(file) as f:
        lines = f.read().splitlines()
    return parse(lines)


def calculate_alignment_cost(positions):
    average = statistics.median(positions)
    return sum(abs(x - average) for x in positions)


def calculate_alignment_cost_complex(positions):
    minimum = min(positions)
    maximum = max(positions)
    min_cost = math.inf
    for final_position in range(minimum, maximum + 1):
        total_cost = 0
        for initial_position in positions:
            n = abs(final_position - initial_position)
            cost = int(n * (n + 1) / 2)
            total_cost += cost
        if total_cost < min_cost:
            min_cost = total_cost
    return min_cost


class MyTest(unittest.TestCase):
    def test_calculate_alignment_cost(self):
        received = calculate_alignment_cost(get_data("test_input.txt"))
        expected = 37
        self.assertEqual(received, expected)

    def test_calculate_alignment_cost_complex_1(self):
        received = calculate_alignment_cost_complex([0, 1, 4])
        expected = 7
        self.assertEqual(received, expected)

    def test_calculate_alignment_cost_complex_2(self):
        received = calculate_alignment_cost_complex(get_data("test_input.txt"))
        expected = 168
        self.assertEqual(received, expected)


if __name__ == "__main__":
    # unittest.main()

    data = get_data("input.txt")
    part1 = calculate_alignment_cost(data)
    part2 = calculate_alignment_cost_complex(data)
    print(part1)
    print(part2)
