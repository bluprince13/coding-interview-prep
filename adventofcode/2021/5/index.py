# https://adventofcode.com/2021/day/5

import unittest
from functools import reduce
import re


def parse_line(string):
    pattern = "(\d+),(\d+) -> (\d+),(\d+)"
    match = re.search(pattern, string)
    return (int(match.group(1)), int(match.group(2))), (
        int(match.group(3)),
        int(match.group(4)),
    )


def parse(lines):
    return [parse_line(line) for line in lines]


def is_orthogonal(line):
    return line[0][0] == line[1][0] or line[0][1] == line[1][1]


def initialise_matrix(lines):
    largest_x = max(max(line[0][0], line[1][0]) for line in lines)
    largest_y = max(max(line[0][1], line[1][1]) for line in lines)
    return [([0] * (largest_x + 1)) for i in range(largest_y + 1)]


def get_orthogonal_lines(lines):
    return [line for line in lines if is_orthogonal(line)]


def get_affected_coordinates(line, horizontal):
    step = 1
    if horizontal:
        start = line[0][0]
        stop = line[1][0]
    else:
        start = line[0][1]
        stop = line[1][1]
    if start > stop:
        step = -1
    affected_coordinates = list(range(start, stop + step, step))
    return affected_coordinates


def get_matrix_of_overlaps(lines):
    matrix = initialise_matrix(lines)
    lines = get_orthogonal_lines(lines)
    for line in lines:
        for i in get_affected_coordinates(line, horizontal=True):
            for j in get_affected_coordinates(line, horizontal=False):
                matrix[j][i] += 1
    return matrix


def find_number_of_overlaps(lines):
    number_of_overlaps = 0
    for line in get_matrix_of_overlaps(lines):
        for number in line:
            if number > 1:
                number_of_overlaps += 1
    return number_of_overlaps


def get_data(file):
    with open(file) as f:
        lines = f.read().splitlines()
    return parse(lines)


class MyTest(unittest.TestCase):
    def test_parse_line(self):
        # 0,9 -> 5,9
        received = parse_line("0,9 -> 5,9")
        expected = (0, 9), (5, 9)
        self.assertEqual(received, expected)

    def test_get_affected_coordinates(self):
        received = get_affected_coordinates(((0, 9), (5, 9)), True)
        expected = [0, 1, 2, 3, 4, 5]
        self.assertEqual(received, expected)

    def test_get_affected_coordinates_single_value(self):
        received = get_affected_coordinates(((0, 9), (5, 9)), False)
        expected = [9]
        self.assertEqual(received, expected)

    def test_get_affected_coordinates_negative(self):
        received = get_affected_coordinates(((5, 9), (0, 9)), True)
        expected = [5, 4, 3, 2, 1, 0]
        self.assertEqual(received, expected)

    def test_find_number_of_overlaps(self):
        received = find_number_of_overlaps(get_data("test_input.txt"))
        expected = 5
        self.assertEqual(received, expected)


if __name__ == "__main__":
    # unittest.main()

    data = get_data("input.txt")
    part1 = find_number_of_overlaps(data)
    part2 = find_number_of_overlaps(data)
    print(part1)
    print(part2)
