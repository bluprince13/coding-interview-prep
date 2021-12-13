# https://adventofcode.com/2021/day/13

# Time taken

# 1st part: > 2h (took me ages to figure out there were two separate operations)
# 2nd part: 45m

# There are two separate operations:
# 1. Reflection: Reflect the coordinates according to the fold.
# 2. Translation: Translate all of the coordinates if some points are now in
#    negative space.

# If the fold is on x axis (e.g. x=5), we only modify the y coordinates
# If the fold is on y axis (e.g. y=5), we only modify the x coordinates

# Example 1
# y1 = 14, y2 = ?
# Fold at reflection line, r = 7
# y1 > r                                        - Only need to reflect if y1 > r
# y2 = r - (y1 - r)
#    = 2r - y1                                  - Formula to apply reflection
#    = 0

# Example 2
# y1 = 14, y2 = ?
# Fold at reflection line, r = 2
# y1 > r
# y2 = -10
# We now have to translate all coordiantes, so that the minimum y is 0
# translation = max(y1) - 2r                    - Formula to calculate translation
#             = 10
# y3 = y2 + translation                         - Formula to apply translation
#    = 0

# Steps
# 1. Calculate translation => max(y) - 2r
# 2. Apply reflection to all coordinates (if y1 > r) => 2r - y1
# 3. Apply translation to all coordinates => y2 + translation

import unittest
import re
import matplotlib.pyplot as plt


def parse_coords(line):
    return list(map(int, line.split(",")))


def parse_folds(line):
    pattern = "([xy])=(\d+)"
    match = re.search(pattern, line)
    return (match.group(1), int(match.group(2)))


def parse_lines(lines):
    empty_line_index = lines.index("")
    coords_lines = lines[:empty_line_index]
    fold_lines = lines[empty_line_index + 1 :]
    coords = [parse_coords(line) for line in coords_lines]
    folds = [parse_folds(line) for line in fold_lines]
    return coords, folds


def get_data(file):
    with open(file) as f:
        lines = f.read().splitlines()
    return parse_lines(lines)


def appy_reflection(coord, r, dimension):
    x = coord[dimension]
    if x > r:
        coord[dimension] = 2 * r - x
    return coord


def apply_translation(coord, translation, dimension):
    x = coord[dimension]
    coord[dimension] = x + translation
    return coord


def get_translation(coords, r, dimension):
    maximum = max(coords, key=lambda coord: coord[dimension])[dimension]
    return max(0, maximum - 2 * r)


def apply_fold(coords, fold, should_sort=False):
    fold_axis = fold[0]
    r = fold[1]

    if fold_axis == "x":
        dimension_to_adjust = 0
    elif fold_axis == "y":
        dimension_to_adjust = 1

    translation = get_translation(coords, r, dimension_to_adjust)

    final_coords = []
    for coord in coords:
        reflected_coord = appy_reflection(coord, r, dimension_to_adjust)
        new_coord = apply_translation(reflected_coord, translation, dimension_to_adjust)
        if coord not in final_coords:
            final_coords.append(new_coord)

    # Sort coords to make it easier to debug, but this is not necessary
    if should_sort:
        final_coords = sorted(final_coords, key=lambda k: [k[0], k[1]])
    return final_coords


def get_visible_dots(coords, folds, number_to_apply=None, plot=False):
    if number_to_apply is None:
        number_to_apply = len(folds)
    for fold in folds[:number_to_apply]:
        coords = apply_fold(coords, fold, should_sort=True)
    if plot:
        print_dots(coords)
    return len(coords)


def print_dots(coords):
    # Invert y and x because the letters come out vertical instead of horizontal
    max_y = max(coords, key=lambda coord: coord[0])[0]
    max_x = max(coords, key=lambda coord: coord[1])[1]
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            # And here we have to invert x and y again
            if [y, x] in coords:
                print("#", end="")
            else:
                print(" ", end="")
        print()


class MyTest(unittest.TestCase):
    def test_get_visible_dots_1(self):
        coords, folds = get_data("test_input.txt")
        received = get_visible_dots(coords, folds, number_to_apply=1)
        expected = 17
        self.assertEqual(received, expected)

    def test_get_visible_dots_2(self):
        coords, folds = get_data("test_input.txt")
        received = get_visible_dots(coords, folds)
        expected = 16
        self.assertEqual(received, expected)


if __name__ == "__main__":
    # unittest.main()

    coords, folds = get_data("input.txt")
    part1 = get_visible_dots(coords, folds, number_to_apply=1)
    print(part1)

    part2 = get_visible_dots(coords, folds, plot=True)

    # #### #  #   ## #  #  ##  #### #  # ###
    #    # #  #    # #  # #  # #    #  # #  #
    #   #  #  #    # #  # #  # ###  #### #  #
    #  #   #  #    # #  # #### #    #  # ###
    # #    #  # #  # #  # #  # #    #  # #
    # ####  ##   ##   ##  #  # #    #  # #
