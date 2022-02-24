# Zalando online assessment - 100%
# Fix bug in code

import unittest


def get_most_frequent_character(S):
    occurrences = [0] * 26

    for i in range(len(S)):
        occurrences[ord(S[i]) - ord("a")] += 1

    best_char = "a"
    best_res = 0

    for i in range(26): # range was 1, 26 initially
        if occurrences[i] > best_res: # operator was >= initially
            best_char = chr(ord("a") + i)
            best_res = occurrences[i]

    return best_char


class MyTest(unittest.TestCase):
    def test_1(self):
        s = "hello"
        received = get_most_frequent_character(s)
        expected = "l"
        self.assertEqual(received, expected)

    def test_2(self):
        s = "helloe"
        received = get_most_frequent_character(s)
        expected = "e"
        self.assertEqual(received, expected)


if __name__ == "__main__":
    unittest.main()
