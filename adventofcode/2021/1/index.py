# https://adventofcode.com/2021/day/1

import unittest


def parse(input_data):
    return list(map(int, input_data))


def get_data():
    with open("./input.txt") as f:
        lines = f.read().splitlines()
    return parse(lines)


def countIncreases(measurements):
    count = 0
    for index, measure in enumerate(measurements):
        if index == 0:
            continue
        if measure > measurements[index - 1]:
            count += 1
    return count


def getSlidingWindowSums(measurements):
    window_size = 3
    sums = []
    for index, _ in enumerate(measurements):
        if index < window_size - 1:
            continue
        sums.append(sum(measurements[index - window_size + 1 : index + 1]))
    return sums


class MyTest(unittest.TestCase):
    def test_1(self):
        measurements = parse(
            ["199", "200", "208", "210", "200", "207", "240", "269", "260", "263"]
        )
        received = countIncreases(measurements)
        expected = 7
        self.assertEqual(received, expected)

    def test_2(self):
        measurements = parse(
            ["199", "200", "208", "210", "200", "207", "240", "269", "260", "263"]
        )
        received = getSlidingWindowSums(measurements)
        expected = [607, 618, 618, 617, 647, 716, 769, 792]
        self.assertEqual(received, expected)


if __name__ == "__main__":
    # unittest.main()

    measurements = parse(get_data())
    part1 = countIncreases(measurements)
    part2 = countIncreases(getSlidingWindowSums(measurements))
    print(part1)
    print(part2)
