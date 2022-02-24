# https://adventofcode.com/2021/day/3

from pathlib import Path
import unittest


def parse(lines):
    return lines


def get_data(file):
    with open(Path(__file__).parent / file) as f:
        lines = f.read().splitlines()
    return parse(lines)


def invert_binary(binary):
    return "".join(([str(1 - int(digit)) for digit in binary]))


def get_zero_counts(diagnostic_report, at_index=None):
    length_of_entry = len(diagnostic_report[0])
    zero_counts = [0 for _ in range(length_of_entry)]
    for entry in diagnostic_report:
        for index, character in enumerate(entry):
            if character == "0":
                zero_counts[index] += 1
    return zero_counts


def get_most_common_values(diagnostic_report):
    zero_counts = get_zero_counts(diagnostic_report)
    num_entries = len(diagnostic_report)
    most_common_values = ""
    for zero_count in zero_counts:
        most_common_values += "0" if zero_count > num_entries / 2 else "1"
    return most_common_values


def get_power_consumption(diagnostic_report):
    gamma_rate_bit = get_most_common_values(diagnostic_report)
    epsilon_rate_bit = invert_binary(gamma_rate_bit)
    gamma_rate = int(gamma_rate_bit, 2)
    epsilon_rate = int(epsilon_rate_bit, 2)
    return gamma_rate * epsilon_rate


def apply_bit_criteria(diagnostic_report, is_least_common_value):
    choices = diagnostic_report
    length_of_entry = len(diagnostic_report[0])

    for index in range(length_of_entry):

        criterion = get_most_common_values(choices)[index]
        if is_least_common_value:
            criterion = str(1 - int(criterion))

        choices = [choice for choice in choices if choice[index] == criterion]
        if len(choices) == 1:
            break
    return int(choices[0], 2)


def get_life_support_rating(diagnostic_report):
    oxygen_generator_rating = apply_bit_criteria(diagnostic_report, False)
    co2_scrubber_rating = apply_bit_criteria(diagnostic_report, True)
    return oxygen_generator_rating * co2_scrubber_rating


class MyTest(unittest.TestCase):
    def test_get_power_consumption(self):
        received = get_power_consumption(get_data("test_input.txt"))
        expected = 198
        self.assertEqual(received, expected)

    def test_get_life_support_rating(self):
        received = get_life_support_rating(get_data("test_input.txt"))
        expected = 230
        self.assertEqual(received, expected)


if __name__ == "__main__":
    # unittest.main()

    diagnostic_report = get_data("input.txt")
    part1 = get_power_consumption(diagnostic_report)
    part2 = get_life_support_rating(diagnostic_report)
    print(part1)
    print(part2)
