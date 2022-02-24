# https://adventofcode.com/2021/day/8

# 0: a  b   c       e   f   g       - 6
# 1:        c           f           - 2 - UNIQUE
# 2: a      c   d   e       g       - 5
# 3: a      c   d       f   g       - 5
# 4:    b   c   d       f           - 4 - UNIQUE
# 5: a  b       d       f   g       - 5
# 6: a  b       d   e   f   g       - 6
# 7: a      c           f           - 3 - UNIQUE
# 8: a  b   c   d   e   f   g       - 7 - UNIQUE
# 9: a  b   c   d       f   g       - 6
#    8  6   8   7   4   9   7       - counts

# Length based deductions
# 5 - 2, 3, 5
# 6 - 0, 6, 9

# Letter count based deductions
# 4 - e
# 6 - b
# 7 - d, g
# 8 - a, c
# 9 - f

# 1. Identify unique length numbers
# 2. Identify e, b, and f based on counts across all patterns
# 3. Identify c - it's the letter that's not f in 1.
# 4. Identify a - it's the letter that appears 8 times that's not c.
# 5. Identify d - it's the remaining unidenified letter in 4.
# 6. Identify g - it's the remaining unidenified letter.

from pathlib import Path
import unittest

real_digit_codes_map = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}


def parse_line(line):
    codes, output = line.split("|")
    codes = [code for code in codes.strip().split(" ")]
    output = [code for code in output.strip().split(" ")]
    return codes, output


def parse_lines(lines):
    return [parse_line(line) for line in lines]


def get_data(file):
    with open(Path(__file__).parent / file) as f:
        lines = f.read().splitlines()
    return parse_lines(lines)


def identify_letters(pattern):
    known_numbers = {}
    known_letters = {}
    letters = ["a", "b", "c", "d", "e", "f", "g"]

    letter_counts = {}
    for letter in letters:
        letter_counts[letter] = 0

    # 1. Identify unique length numbers
    for code in pattern:
        digit = identify_digit(code)
        if digit is not None:
            known_numbers[digit] = code

    # 2. Identify e, b, and f based on counts across all patterns
    for code in pattern:
        for letter in letters:
            if letter in code:
                letter_counts[letter] += 1

    for letter in letters:
        count = letter_counts[letter]
        if count == 4:
            known_letters["e"] = letter
        elif count == 6:
            known_letters["b"] = letter
        elif count == 9:
            known_letters["f"] = letter

    # 3. Identify c - it's the letter that's not f in 1.
    known_letters["c"] = known_numbers[1].replace(known_letters["f"], "")

    # 4. Identify a - it's the letter that appears 8 times that's not c.
    letter_with_count_8 = [letter for letter in letters if letter_counts[letter] == 8]
    letter_with_count_8.remove(known_letters["c"])
    assert len(letter_with_count_8) == 1
    known_letters["a"] = letter_with_count_8[0]

    # 5. Identify d - it's the remaining unidentified letter in 4.
    unidentified_letters_in_4 = [
        letter for letter in known_numbers[4] if letter not in known_letters.values()
    ]
    assert len(unidentified_letters_in_4) == 1
    known_letters["d"] = unidentified_letters_in_4[0]

    # 6. Identify g - it's the remaining unidentified letter.
    remaining_letters = [
        letter for letter in letters if letter not in known_letters.values()
    ]
    assert len(remaining_letters) == 1
    known_letters["g"] = remaining_letters[0]

    return dict((v, k) for k, v in known_letters.items())


def get_correct_code(code, known_letters):
    correct_code = []
    for letter in code:
        correct_code.append(known_letters[letter])
    return "".join(sorted(correct_code))


def identify_digit(code, known_letters=None):
    length = len(code)
    if length == 2:
        return 1
    elif length == 4:
        return 4
    elif length == 3:
        return 7
    elif length == 7:
        return 8

    if known_letters is not None:
        correct_code = get_correct_code(code, known_letters)
        if correct_code in real_digit_codes_map:
            return real_digit_codes_map[correct_code]


def is_1478(code):
    matches = [1, 4, 7, 8]
    return identify_digit(code) in matches


def count_1478_in_output(output):
    return len([code for code in output if is_1478(code)])


def count_1478(outputs):
    return sum([count_1478_in_output(output) for output in outputs])


def get_digit_codes_map(codes):
    known_letters = identify_letters(codes)
    digit_codes_map = {}
    for code in codes:
        sorted_code = "".join(sorted(code))
        digit_codes_map[sorted_code] = identify_digit(code, known_letters)
    return digit_codes_map


def decode_output(output, digit_codes_map):
    digits = []
    for code in output:
        sorted_code = "".join(sorted(code))
        digit = digit_codes_map[sorted_code]
        digits.append(str(digit))
    decoded_output = "".join(digits)
    return int(decoded_output)


def get_sum_of_outputs(entries):
    decoded_outputs = []
    for entry in entries:
        codes, output = entry
        digit_codes_map = get_digit_codes_map(codes)
        decoded_outputs.append(decode_output(output, digit_codes_map))
    return sum(decoded_outputs)


class MyTest(unittest.TestCase):
    def test_count_1478(self):
        entries = get_data("test_input.txt")
        outputs = [output for _, output in entries]
        received = count_1478(outputs)
        expected = 26
        self.assertEqual(received, expected)

    def test_get_digit_patterns(self):
        codes = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab".split(" ")
        received = get_digit_codes_map(codes)
        expected = {
            "abcdefg": 8,
            "bcdef": 5,
            "acdfg": 2,
            "abcdf": 3,
            "abd": 7,
            "abcdef": 9,
            "bcdefg": 6,
            "abef": 4,
            "abcdeg": 0,
            "ab": 1,
        }
        self.assertEqual(received, expected)

    def test_get_sum_of_outputs(self):
        entries = get_data("test_input.txt")
        received = get_sum_of_outputs(entries)
        expected = 61229
        self.assertEqual(received, expected)


if __name__ == "__main__":
    # unittest.main()

    entries = get_data("input.txt")
    outputs = [output for _, output in entries]
    part1 = count_1478(outputs)
    print(part1)

    part2 = get_sum_of_outputs(entries)
    print(part2)
