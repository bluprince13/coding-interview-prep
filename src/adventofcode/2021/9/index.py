# https://adventofcode.com/2021/day/9

import unittest
import math


def parse_line(line):
    return [int(number) for number in line]


def parse_lines(lines):
    return [parse_line(line) for line in lines]


def get_data(file):
    with open(file) as f:
        lines = f.read().splitlines()
    return parse_lines(lines)


def get_height(height_map, coord):
    return height_map[coord[0]][coord[1]]


def get_neighbours(coord, height_map):
    x, y = coord

    neighbours = []
    neighbour_coords = []
    if y > 0:
        neighbour_coords.append((x, y - 1))
    if y < len(height_map[x]) - 1:
        neighbour_coords.append((x, y + 1))
    if x > 0:
        neighbour_coords.append((x - 1, y))
    if x < len(height_map) - 1:
        neighbour_coords.append((x + 1, y))

    for neighbour_coord in neighbour_coords:
        neighbour = get_height(height_map, neighbour_coord)
        neighbours.append(neighbour)

    return neighbours, neighbour_coords


def get_height_diff_map(height_map):
    height_diff_map = []
    for x, line in enumerate(height_map):
        line_diff_map = []
        for y, height in enumerate(line):
            neighbour_heights, _ = get_neighbours((x, y), height_map)
            height_diff = min(neighbour_heights) - height
            line_diff_map.append(height_diff)
        height_diff_map.append(line_diff_map)
    return height_diff_map


def get_low_points(height_map):
    low_points = []
    low_point_coords = []
    height_diff_map = get_height_diff_map(height_map)

    for x, line in enumerate(height_diff_map):
        for y, height_diff in enumerate(line):
            if height_diff > 0:
                low_points.append(height_map[x][y])
                low_point_coords.append((x, y))
    return low_points, low_point_coords


def get_risk_level(height_map):
    low_points, _ = get_low_points(height_map)
    return sum(low_points) + len(low_points)


def get_basin_coords(height_map, coord, basin_coords=[]):
    basin_coords = basin_coords.copy()
    if coord not in basin_coords:
        basin_coords.append(coord)
    _, neighbours_coords = get_neighbours(coord, height_map)
    for neighbour_coord in neighbours_coords:
        if (
            neighbour_coord not in basin_coords
            and get_height(height_map, neighbour_coord) != 9
        ):
            basin_coords.append(neighbour_coord)
            basin_coords = get_basin_coords(height_map, neighbour_coord, basin_coords)
    return basin_coords


def get_basin_sizes(height_map):
    _, low_point_coords = get_low_points(height_map)
    basin_sizes = []

    for low_point_coord in low_point_coords:
        basin_coords = get_basin_coords(height_map, low_point_coord)
        basin_size = len(basin_coords)
        basin_sizes.append(basin_size)

    return sorted(basin_sizes)


def get_three_largest_basins(height_map):
    basin_sizes = get_basin_sizes(height_map)
    return math.prod(basin_sizes[-3:])


class MyTest(unittest.TestCase):
    def test_get_risk_level(self):
        height_map = get_data("test_input.txt")
        received = get_risk_level(height_map)
        expected = 15
        self.assertEqual(received, expected)

    def test_get_basin_coords(self):
        height_map = get_data("test_input.txt")
        received = get_basin_coords(height_map, (0, 1))
        expected = [(0, 0), (0, 1), (1, 0)]
        self.assertEqual(set(received), set(expected))

    def test_get_basin_sizes(self):
        height_map = get_data("test_input.txt")
        received = get_basin_sizes(height_map)
        expected = [3, 9, 9, 14]
        self.assertEqual(received, expected)

    def test_get_three_largest_basins(self):
        height_map = get_data("test_input.txt")
        received = get_three_largest_basins(height_map)
        expected = 1134
        self.assertEqual(received, expected)


if __name__ == "__main__":
    # unittest.main()

    height_map = get_data("input.txt")
    part1 = get_risk_level(height_map)
    print(part1)

    part2 = get_three_largest_basins(height_map)
    print(part2)
