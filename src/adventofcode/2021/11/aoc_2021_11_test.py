# https://adventofcode.com/2021/day/11

# Time taken
# 1st part: 0 h 56 m
# 2nd part: 0 h 14 m

from pathlib import Path
import unittest
import itertools
import copy

def parse_line(line):
    return [int(energy) for energy in line]


def parse_lines(lines):
    return [parse_line(line) for line in lines]


def get_data(file):
    with open(Path(__file__).parent / file) as f:
        lines = f.read().splitlines()
    return parse_lines(lines)


def count_flashes(energy_levels):
    return sum(1 for energy in itertools.chain(*energy_levels) if energy == 0)


def get_energy_level(energy_levels, coord):
    return energy_levels[coord[0]][coord[1]]


def get_unflashed_neighbours(energy_levels, coord):
    x, y = coord
    last_position = len(energy_levels[0]) - 1
    neighbour_coords = []
    unflashed_neighbour_coords = []

    if y > 0:
        neighbour_coords.append((x, y - 1))
    if y < last_position:
        neighbour_coords.append((x, y + 1))
    if x > 0:
        neighbour_coords.append((x - 1, y))
    if x < last_position:
        neighbour_coords.append((x + 1, y))
    if y > 0 and x > 0:
        neighbour_coords.append((x - 1, y - 1))
    if y > 0 and x < last_position:
        neighbour_coords.append((x + 1, y - 1))
    if y < last_position and x > 0:
        neighbour_coords.append((x - 1, y + 1))
    if y < last_position and x < last_position:
        neighbour_coords.append((x + 1, y + 1))

    for neighbour_coord in neighbour_coords:
        energy_level = get_energy_level(energy_levels, neighbour_coord)
        if energy_level != 0:
            unflashed_neighbour_coords.append(neighbour_coord)

    return unflashed_neighbour_coords


def get_all_cords(energy_levels):
    coords = []
    for row_index, row in enumerate(energy_levels):
        for column_index, energy_level in enumerate(row):
            coord = row_index, column_index
            coords.append(coord)
    return coords


def run_flashes_for_step(energy_levels, flash_count=0, coords=[]):
    if not coords:
        coords = get_all_cords(energy_levels)
    for coord in coords:

        # Flash any > 9
        x, y = coord
        energy_level = get_energy_level(energy_levels, coord)
        if energy_level > 9:
            energy_levels[x][y] = 0
            flash_count += 1

            # Modify neighbours and flash again if necessary
            unflashed_neighbours = get_unflashed_neighbours(energy_levels, coord)
            for neighbour_coord in unflashed_neighbours:
                x, y = neighbour_coord
                energy_levels[x][y] += 1

            energy_levels, flash_count = run_flashes_for_step(
                energy_levels, flash_count, unflashed_neighbours
            )

    return energy_levels, flash_count


def get_flash_count(energy_levels, steps=None):
    energy_levels = copy.deepcopy(energy_levels)
    coords = get_all_cords(energy_levels)
    flash_count_simulation = 0
    step = 1

    while True:
        step += 1
        # Increment all energy levels by 1 at start of simulation
        for x, y in coords:
            energy_levels[x][y] += 1

        # Run flashes for step
        energy_levels, flash_count = run_flashes_for_step(energy_levels)
        flash_count_simulation += flash_count

        if steps is not None:
            if step == steps + 1:
                break
        else:
            if count_flashes(energy_levels) == 100:
                break

    return flash_count_simulation, step - 1


class MyTest(unittest.TestCase):
    def test_get_flash_count_1(self):
        received, _ = get_flash_count(get_data("test_input.txt"), 2)
        expected = 35
        self.assertEqual(received, expected)

    def test_get_flash_count_2(self):
        received, _ = get_flash_count(get_data("test_input.txt"), 3)
        expected = 35 + 45
        self.assertEqual(received, expected)

    def test_get_flash_count_3(self):
        received, _ = get_flash_count(get_data("test_input.txt"), 10)
        expected = 204
        self.assertEqual(received, expected)

    def test_get_flash_count_4(self):
        received, _ = get_flash_count(get_data("test_input.txt"), 100)
        expected = 1656
        self.assertEqual(received, expected)

    def test_get_flash_count_breaks_at_simultaneous_flash(self):
        _, received = get_flash_count(get_data("test_input.txt"), None)
        expected = 195
        self.assertEqual(received, expected)

if __name__ == "__main__":
    # unittest.main()

    energy_levels = get_data("input.txt")
    part1 = get_flash_count(energy_levels, 100)
    print(part1)

    part2 = get_flash_count(energy_levels, None)
    print(part2)
