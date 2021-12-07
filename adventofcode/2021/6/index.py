# https://adventofcode.com/2021/day/6

# Example:
# Day -: 0, 8            Two breeders: adult A and newborn B
# Day 1: 6, 7, 8         An adult A gives birth (7 days later)
# Day 2: 5, 6, 7
# Day 3: 4, 5, 6
# Day 4: 3, 4, 5
# Day 5: 2, 3, 4
# Day 6: 1, 2, 3
# Day 7: 0, 1, 2
# Day 8: 6, 0, 1, 8      An adult A gives birth to newborn C (7 days later)
# Day 9: 5, 6, 0, 7
# Day 10: 4, 5, 6, 6, 8  A newborn B gives birth to newborn D (9 days later),
#                        and becomes an adult

# Index    0  1  2  3  4  5  6  7  8
# Day - = [1, 0, 0, 0, 0, 0, 0, 0, 1] = 2 - Initial count of population by timer
# Day 1 = [0, 0, 0, 0, 0, 0, 1, 1, 1] = 3
# Day 2 = [0, 0, 0, 0, 0, 1, 1, 1, 0] = 3
# Day 3 = [0, 0, 0, 0, 1, 1, 1, 0, 0] = 3
# ...
# Day 7 = [1, 1, 1, 0, 0, 0, 0, 0, 0] = 3
# Day 8 = [1, 1, 0, 0, 0, 0, 1, 0, 1] = 4

import unittest
import copy

def parse(lines):
    return list(map(int, lines[0].split(",")))


def get_data(file):
    with open(file) as f:
        lines = f.read().splitlines()
    return parse(lines)


def get_population_brute_force(timers, cycles):
    timers = copy.copy(timers)
    for _ in range(cycles):
        count_zeros = 0
        for index, timer in enumerate(timers):
            if timer == 0:
                timers[index] = 6
                count_zeros += 1
            else:
                timers[index] -= 1
        timers.extend([8] * count_zeros)
    return len(timers)


def get_population_optimised(timers, cycles):
    period = 9
    population_by_age = [0] * period

    # Initialise population
    for timer in timers:
        population_by_age[timer] += 1

    # Simulate cycles
    for _ in range(cycles):
        new_population = [0] * period
        for index, _ in enumerate(population_by_age):
            if index < 8:
                new_population[index] = population_by_age[index + 1]
            else:
                new_population[index] = population_by_age[0]
            if index == 6:
                new_population[index] += population_by_age[0]
        population_by_age = new_population
    return sum(new_population)


class MyTest(unittest.TestCase):
    def test_get_population_brute_force(self):
        received = get_population_brute_force(get_data("test_input.txt"), 18)
        expected = 26
        self.assertEqual(received, expected)

    def test_get_population_optimised_1(self):
        received = get_population_optimised([0, 8], 8)
        expected = 4
        self.assertEqual(received, expected)

    def test_get_population_optimised_2(self):
        received = get_population_optimised(get_data("test_input.txt"), 18)
        expected = 26
        self.assertEqual(received, expected)


if __name__ == "__main__":
    # unittest.main()

    data = get_data("input.txt")
    part1 = get_population_brute_force(data, 80)
    part2 = get_population_optimised(data, 256)
    print(part1)
    print(part2)
