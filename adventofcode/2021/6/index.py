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

# In the above example, adult A can be counted on to always give birth every 7
# days. i.e. A will always give birth day 1 of a 9 day cycle.

# If we track number of breeders today, we know they will breed again on:
#   Day 9 for newborns
#   Day 7 for adults

# Index    0  1  2  3  4  5  6  7  8
# Day - = [1, 0, 0, 0, 0, 0, 0, 0, 1] = 2
# Day 1 = [1, 0, 0, 0, 0, 0, 0, 1, 1] = 3 - Count at 7 incremented by count at 0
# Day 2 = [1, 0, 0, 0, 0, 0, 0, 1, 1] = 3
# Day 3 = [1, 0, 0, 0, 0, 0, 0, 1, 1] = 3
# Day 4 = [1, 0, 0, 0, 0, 0, 0, 1, 1] = 3
# Day 5 = [1, 0, 0, 0, 0, 0, 0, 1, 1] = 3
# Day 6 = [1, 0, 0, 0, 0, 0, 0, 1, 1] = 3
# Day 7 = [1, 0, 0, 0, 0, 0, 0, 1, 1] = 3
# Day 8 = [1, 0, 0, 0, 0, 1, 0, 1, 1] = 4 - Count at 5 incremented by count at 7
# Day 9 = [1, 0, 0, 0, 0, 1, 1, 1, 1] = 5 - Count at 6 incremented by count at 8
# Day 10 = [1, 0, 0, 0, 0, 1, 1, 2, 1] = 5 - Count at 7 incremented by count at 0


import unittest


def parse(lines):
    return list(map(int, lines[0].split(",")))


def get_data(file):
    with open(file) as f:
        lines = f.read().splitlines()
    return parse(lines)


def get_population_brute_force(timers, cycles):
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
    for cycle in range(cycles):
        # Take the modulus: e.g. 7 % 9 = 7
        # cycle_day      : 0, 1, 2, 3, 4, 5, 6, 7, 8
        cycle_day = cycle % period

        # increment at   : 7, 8, 0, 1, 2, 3, 4, 5, 6
        group_to_increment = (cycle_day + 7) % period
        population_by_age[group_to_increment] += population_by_age[cycle_day]
    return sum(population_by_age)


class MyTest(unittest.TestCase):
    # def test_get_population_brute_force(self):
    #     received = get_population_brute_force(get_data("test_input.txt"), 18)
    #     expected = 26
    #     self.assertEqual(received, expected)

    def test_get_population_optimised(self):
        received = get_population_optimised([0, 8], 10)
        expected = 6
        self.assertEqual(received, expected)

    # def test_get_population_optimised(self):
    #     received = get_population_optimised(get_data("test_input.txt"), 18)
    #     expected = 26
    #     self.assertEqual(received, expected)


if __name__ == "__main__":
    unittest.main()

    # data = get_data("input.txt")
    # part1 = get_population_brute_force(data, 80)

    # data = get_data("input.txt")
    # part2 = get_population_optimised(data, 256)

    # print(part1)
    # print(part2)
