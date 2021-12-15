# https://adventofcode.com/2021/day/15

# Time taken
# 1st part:
# 2nd part:

import unittest
import networkx as nx


def parse_line(line):
    return [int(number) for number in line]


def parse_lines(lines):
    return [parse_line(line) for line in lines]


def get_all_cords(data):
    coords = []
    for row_index, row in enumerate(data):
        for column_index, _ in enumerate(row):
            coord = row_index, column_index
            coords.append(coord)
    return coords


def generate_graph(data, end_node):
    G = nx.DiGraph()
    coords = get_all_cords(data)
    for x, y in coords:
        if x > 0:
            G.add_edge((x - 1, y), (x, y), weight=data[y][x])
        if x < len(data[::-1]) - 1:
            G.add_edge((x + 1, y), (x, y), weight=data[y][x])
        if y > 0:
            G.add_edge((x, y - 1), (x, y), weight=data[y][x])
        if y < end_node[1]:
            G.add_edge((x, y + 1), (x, y), weight=data[y][x])
    return G


def get_data(file, full_map=False):
    with open(file) as f:
        lines = f.read().splitlines()
    lines = parse_lines(lines)
    lines = get_full_map(lines) if full_map else lines
    return lines


def get_full_map(data):
    length_tile = len(data[::-1])
    new_data = []
    for i in range(length_tile * 5):
        row = []
        for j in range(length_tile * 5):
            original_value = data[i % 10][j % 10]
            if j < 10 and i < 10:
                new_value = original_value
            else:
                if j > 9:
                    previous_value = row[j - 10]
                elif i > 9:
                    previous_value = new_data[i - 10][j]
                new_value = previous_value + 1
                if new_value > 9:
                    new_value = 1
            row.append(new_value)
        new_data.append(row)
    return new_data


def print_data(data):
    for row in data:
        print("".join(str(x) for x in row))


def get_lowest_risk(data, full_map=False):
    data = get_full_map(data) if full_map else data

    start_node = 0, 0
    end_node = len(data) - 1, len(data[0]) - 1

    G = generate_graph(data, end_node)
    lowest_risk = nx.shortest_path_length(G, start_node, end_node, weight="weight")
    return lowest_risk


class MyTest(unittest.TestCase):
    def test_get_lowest_risk_1(self):
        data = get_data("test_input.txt")
        received = get_lowest_risk(data)
        expected = 40
        self.assertEqual(received, expected)

    def test_get_lowest_risk_2(self):
        data = get_data("input.txt")
        received = get_lowest_risk(data)
        expected = 604
        self.assertEqual(received, expected)

    def test_get_full_map(self):
        data = get_data("test_input.txt")
        received = get_full_map(data)
        expected = get_data("expected_full_map.txt")
        self.assertEqual(received, expected)

    def test_get_lowest_risk_full_map(self):
        data = get_data("test_input.txt")
        received = get_lowest_risk(data, full_map=True)
        expected = 315
        self.assertEqual(received, expected)



if __name__ == "__main__":
    # unittest.main()

    data = get_data("input.txt")
    part1 = get_lowest_risk(data)
    print(part1)

    part2 = get_lowest_risk(data, full_map=True)
    print(part2)
