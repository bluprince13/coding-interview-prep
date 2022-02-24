# https://adventofcode.com/2021/day/14

# Time taken

# 1st part: 1h 0m
# 2nd part: 0h 2m

# NNCB
#  3 pairs, length = 4

# NCNBCHB
# NN -> C => NC and CN
# NC -> B => NB and BC
# CB -> H => CH and HC
# 6 pairs, length = 7

# At each iteration, each pair leads to two new pairs.

from pathlib import Path
import unittest
import re


def parse_coords(line):
    return list(map(int, line.split(",")))


def parse_rule(line):
    pattern = "([A-Z]{2}) -> ([A-Z])"
    match = re.search(pattern, line)
    return (match.group(1), match.group(2))


def parse_lines(lines):
    polymer = lines[0]
    rules = [parse_rule(line) for line in lines[2:]]
    return polymer, rules


def get_data(file):
    with open(Path(__file__).parent / file) as f:
        lines = f.read().splitlines()
    return parse_lines(lines)


def get_pairs_map(polymer):
    pairs = [polymer[i : i + 2] for i in range(len(polymer) - 1)]
    pairs_map = {}
    for pair in pairs:
        if pair in pairs_map:
            pairs_map[pair] += 1
        else:
            pairs_map[pair] = 1
    return pairs_map


def get_rules_map(rules):
    rules_map = {}
    for rule in rules:
        pair = rule[0]
        new_element = rule[1]
        new_pairs = [pair[0] + new_element, new_element + pair[1]]
        rules_map[pair] = new_pairs
    return rules_map


def do_pair_insertion(polymer_map, rules_map):
    new_polymer_map = {}
    for polymer in polymer_map:
        new_pairs = rules_map[polymer]
        for new_pair in new_pairs:
            if new_pair in new_polymer_map:
                new_polymer_map[new_pair] += polymer_map[polymer]
            else:
                new_polymer_map[new_pair] = polymer_map[polymer]
    return new_polymer_map


def grow_polymer(polymer, rules, steps):
    rules_map = get_rules_map(rules)
    pairs_map = get_pairs_map(polymer)
    for _ in range(steps):
        pairs_map = do_pair_insertion(pairs_map, rules_map)
    return pairs_map


def get_element_count(pairs_map, original_polymer):
    element_map = {}
    last_letter = original_polymer[-1]
    for pair in pairs_map:
        letter = pair[0]
        if letter in element_map:
            element_map[letter] += pairs_map[pair]
        else:
            element_map[letter] = pairs_map[pair]
    if last_letter in element_map:
        element_map[last_letter] += 1
    else:
        element_map[last_letter] = 1
    return element_map


def find_least_and_most_common_count_difference(element_map):
    most_common_count = max(element_map.values())
    least_common_count = min(element_map.values())
    return most_common_count - least_common_count


def predict_polymer_growth(polymer, rules, steps=10):
    pairs_map = grow_polymer(polymer, rules, steps)
    element_map = get_element_count(pairs_map, polymer)
    return find_least_and_most_common_count_difference(element_map)


class MyTest(unittest.TestCase):
    def test_solve_part_1(self):
        polymer, rules = get_data("test_input.txt")
        received = predict_polymer_growth(polymer, rules)
        expected = 1588
        self.assertEqual(received, expected)


if __name__ == "__main__":
    # unittest.main()

    polymer, rules = get_data("input.txt")
    part1 = predict_polymer_growth(polymer, rules)
    print(part1)

    part2 = predict_polymer_growth(polymer, rules, 40)
    print(part2)