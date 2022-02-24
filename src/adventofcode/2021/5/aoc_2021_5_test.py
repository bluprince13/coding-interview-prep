# https://adventofcode.com/2021/day/5

from pathlib import Path
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


def get_data(file):
    with open(Path(__file__).parent / file) as f:
        lines = f.read().splitlines()
    return parse(lines)


def is_orthogonal(line):
    return line[0][0] == line[1][0] or line[0][1] == line[1][1]


def get_orthogonal_lines(lines):
    return [line for line in lines if is_orthogonal(line)]


def is_horizontal(line):
    return line[0][0] == line[1][0]


def initialise_matrix(lines):
    largest_x = max(max(line[0][0], line[1][0]) for line in lines)
    largest_y = max(max(line[0][1], line[1][1]) for line in lines)
    return [([0] * (largest_y + 1)) for i in range(largest_x + 1)]


def get_coordinates(line):
    coordinates = []

    ystart = line[0][1]
    ystop = line[1][1]
    ystep = -1 if ystart > ystop else 1

    xstart = line[0][0]
    xstop = line[1][0]
    xstep = -1 if xstart > xstop else 1

    if is_orthogonal(line):
        for x in range(xstart, xstop + xstep, xstep):
            for y in range(ystart, ystop + ystep, ystep):
                coordinates.append((x, y))
    else:
        for x, y in zip(
            range(xstart, xstop + xstep, xstep), range(ystart, ystop + ystep, ystep)
        ):
            coordinates.append((x, y))

    return coordinates


def get_matrix_of_overlaps(lines, should_ignore_diagonals=True):
    matrix = initialise_matrix(lines)
    if should_ignore_diagonals:
        lines = get_orthogonal_lines(lines)
    for line in lines:
        for x, y in get_coordinates(line):
            matrix[x][y] += 1
    return matrix


def find_number_of_overlaps(lines, should_ignore_diagonals=True):
    number_of_overlaps = 0
    for line in get_matrix_of_overlaps(lines, should_ignore_diagonals):
        for number in line:
            if number > 1:
                number_of_overlaps += 1
    return number_of_overlaps


class MyTest(unittest.TestCase):
    def test_parse_line(self):
        # 0,9 -> 5,9
        received = parse_line("0,9 -> 5,9")
        expected = (0, 9), (5, 9)
        self.assertEqual(received, expected)

    def test_get_coordinates_horizontal(self):
        received = get_coordinates(((0, 0), (0, 2)))
        expected = [(0, 0), (0, 1), (0, 2)]
        self.assertEqual(received, expected)

    def test_get_coordinates_horizontal_reverse(self):
        received = get_coordinates(((0, 2), (0, 0)))
        expected = [(0, 2), (0, 1), (0, 0)]
        self.assertEqual(received, expected)

    def test_get_coordinates_vertical(self):
        received = get_coordinates(((0, 0), (2, 0)))
        expected = [(0, 0), (1, 0), (2, 0)]
        self.assertEqual(received, expected)

    def test_get_coordinates_diagonal(self):
        received = get_coordinates(((0, 0), (2, 2)))
        expected = [(0, 0), (1, 1), (2, 2)]
        self.assertEqual(received, expected)

    def test_find_number_of_overlaps_orthogonal_only(self):
        received = find_number_of_overlaps(get_data("test_input.txt"))
        expected = 5
        self.assertEqual(received, expected)

    def test_find_number_of_overlaps_including_diagonals(self):
        received = find_number_of_overlaps(get_data("test_input.txt"), False)
        expected = 12
        self.assertEqual(received, expected)


if __name__ == "__main__":
    # unittest.main()

    data = get_data("input.txt")
    part1 = find_number_of_overlaps(data)
    part2 = find_number_of_overlaps(data, False)
    print(part1)
    print(part2)
