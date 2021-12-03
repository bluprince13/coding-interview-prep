# https://adventofcode.com/2021/day/3

import unittest


def parse(lines):
    return lines


def get_data(file):
    with open(file) as f:
        lines = f.read().splitlines()
    return parse(lines)

def invert_binary(binary):
    return "".join(([str(1 - int(digit)) for digit in binary]))


def calculatePowerConsumption(diagnostic_report):
    gamma_rate_bit = ''

    num_entries = len(diagnostic_report)
    zeros = [0 for _ in range(len(diagnostic_report[0]))]
    for entry in diagnostic_report:
        for index, character in enumerate(entry):
            if character == "0":
                zeros[index] += 1

    for zero_count in zeros:
        gamma_rate_bit += "0" if zero_count > num_entries/2  else "1"

    epsilon_rate_bit = invert_binary(gamma_rate_bit)
    gamma_rate = int(gamma_rate_bit, 2)
    epsilon_rate = int(epsilon_rate_bit, 2)
    return gamma_rate * epsilon_rate


class MyTest(unittest.TestCase):
    def test_1(self):
        received = calculatePowerConsumption(get_data("test_input.txt"))
        expected = 198
        self.assertEqual(received, expected)


if __name__ == "__main__":
    # unittest.main()

    part1 = calculatePowerConsumption(get_data('input.txt'))
    part2 = calculatePowerConsumption(get_data('input.txt'))
    print(part1)
    print(part2)
