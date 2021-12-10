# https://adventofcode.com/2021/day/10

# Time taken
# 1st part: 32 min
# 2nd part: 39 min

import unittest
import statistics

bracket_value_map = {")": 3, "]": 57, "}": 1197, ">": 25137, None: 0}

bracket_completion_value_map = {"(": 1, "[": 2, "{": 3, "<": 4, None: 0}


def parse_line(line):
    return [bracket for bracket in line]


def parse_lines(lines):
    return [parse_line(line) for line in lines]


def get_data(file):
    with open(file) as f:
        lines = f.read().splitlines()
    return parse_lines(lines)


def find_corruption(s):
    stack = []
    openBrackets = "({[<"
    closedBrackets = ")}]>"
    corruption = None

    for character in s:
        if character in openBrackets:
            stack.append(character)
        elif stack and character in closedBrackets:
            lastCharacterInStack = stack[-1]
            if openBrackets.find(lastCharacterInStack) == closedBrackets.find(
                character
            ):
                stack.pop()
            else:
                if corruption is None:
                    corruption = character
        else:
            # if the stack is empty and the character is a closing bracket
            if corruption is None:
                corruption = character

            # check if the stack has open brackets left
    if stack:
        return corruption, "".join(stack)  # Not balanced
    else:
        return corruption, None


def get_syntax_error_score(chunks):
    score = 0
    for chunk in chunks:
        if find_corruption(chunk):
            score += bracket_value_map[find_corruption(chunk)[0]]
    return score


def get_incomplete_lines(chunks):
    incomplete_lines = []
    for chunk in chunks:
        corruption, stack = find_corruption(chunk)
        if stack and corruption is None:
            incomplete_lines.append(stack)
    return incomplete_lines


def get_completion_score(line):
    score = 0
    for bracket in line:
        score = score * 5 + bracket_completion_value_map[bracket]
    return score


def get_completion_score_for_chunks(chunks):
    incomplete_lines = get_incomplete_lines(chunks)
    scores = []
    for line in incomplete_lines:
        scores.append(get_completion_score(line[::-1]))
    return statistics.median(scores)


class MyTest(unittest.TestCase):
    def test_find_corruption_finds_None_if_valid(self):
        valid_chunks = ["()", "[()()]"]
        for chunk in valid_chunks:
            self.assertIsNone(find_corruption(chunk)[0])

    def test_find_corruption_finds_bracket_if_corrupted(self):
        corrupted_chunks = ["(]", "{()()()>"]
        expecteds = ["]", ">"]
        for chunk, expected in zip(corrupted_chunks, expecteds):
            received, _ = find_corruption(chunk)
            self.assertEqual(received, expected)

    def test_get_syntax_error_score(self):
        chunks = get_data("test_input.txt")
        expected = 26397
        received = get_syntax_error_score(chunks)
        self.assertEqual(received, expected)

    def test_get_incomplete_lines(self):
        chunks = ["(", "{()()()}<(){"]
        expected = ["(", "<{"]
        received = get_incomplete_lines(chunks)
        self.assertEqual(received, expected)

    def test_get_completion_score(self):
        line = "[({<"
        expected = 294
        received = get_completion_score(line)
        self.assertEqual(received, expected)

    def test_get_completion_score_for_chunks(self):
        chunks = get_data("test_input.txt")
        expected = 288957
        received = get_completion_score_for_chunks(chunks)
        self.assertEqual(received, expected)


if __name__ == "__main__":
    # unittest.main()

    chunks = get_data("input.txt")
    part1 = get_syntax_error_score(chunks)
    print(part1)

    part2 = get_completion_score_for_chunks(chunks)
    print(part2)
