# https://adventofcode.com/2021/day/12

# Time taken
# 1st part: 3h 30m
# 2nd part: 1h 01m

from pathlib import Path
import unittest
import networkx as nx


def parse_line(line):
    return line.split("-")


def parse_lines(lines):
    return [parse_line(line) for line in lines]


def get_data(file):
    with open(Path(__file__).parent / file) as f:
        lines = f.read().splitlines()
    lines = parse_lines(lines)
    G = nx.Graph()
    G.add_edges_from(lines)
    # nx.draw_networkx(G)
    return G


def get_paths(
    G,
    current_node="start",
    destination_node="end",
    path=[],
    paths=[],
    small_cave_visitable_twice="",
):
    # TODO: Why did I have to use path.copy() here?
    path = path.copy()

    neighbors = list(G.neighbors(current_node))
    path.append(current_node)

    # Remove any small letter neighbors already seen before
    valid_neighbors = []
    for neighbor in neighbors:
        count_neighbour_in_path = path.count(neighbor)

        max_count = 1
        if neighbor == small_cave_visitable_twice:
            max_count = 2

        if neighbor.isupper() or count_neighbour_in_path < max_count:
            valid_neighbors.append(neighbor)

    neighbors = valid_neighbors

    #  If it's a destination node, add the path to the list of paths
    if current_node == destination_node:
        paths.append(path)
        return path, paths

    # If it's a leaf node, don't do anything
    if len(neighbors) == 0:
        return path, paths

    # Otherwise, recurse
    for node in neighbors:
        _, paths = get_paths(
            G, node, destination_node, path, paths, small_cave_visitable_twice
        )

    return path, paths


def get_count_of_paths(G):
    _, paths = get_paths(G)
    return len(paths)


def get_small_caves(G):
    caves = list(G)
    caves.remove("start")
    caves.remove("end")
    return [node for node in caves if node.islower()]


def get_count_of_paths_special(G):
    small_caves = get_small_caves(G)
    all_paths = []
    for small_cave in small_caves:
        _, paths = get_paths(G, small_cave_visitable_twice=small_cave)
        all_paths.extend(paths)
    unique_paths = [list(x) for x in set(tuple(x) for x in all_paths)]
    return len(unique_paths)


class MyTest(unittest.TestCase):
    def test_get_count_of_paths(self):
        G = get_data("test_input.txt")
        received = get_count_of_paths(G)
        expected = 10
        self.assertEqual(received, expected)

    def test_get_count_of_paths_special(self):
        G = get_data("test_input.txt")
        received = get_count_of_paths_special(G)
        expected = 36
        self.assertEqual(received, expected)


if __name__ == "__main__":
    # unittest.main()

    G = get_data("input.txt")
    part1 = get_count_of_paths(G)
    print(part1)

    part2 = get_count_of_paths_special(G)
    print(part2)
