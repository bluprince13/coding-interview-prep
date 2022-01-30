# Zalando online assessment - 100%

import unittest


def parse(s):
    return [int(x) for x in s]


def solution(S):
    digits = parse(S)
    sum_of_digits = sum(digits)
    count = 0

    if sum_of_digits % 3 == 0:
        count += 1

    for digit in digits:
        sum_remaining = sum_of_digits - digit
        for i in range(10):
            new_sum = sum_remaining + i
            if new_sum % 3 == 0 and i != digit:
                count += 1
    return count


class MyTest(unittest.TestCase):
    def test_1(self):
        s = "23"
        received = solution(s)
        expected = 7
        self.assertEqual(received, expected)

    def test_2(self):
        s = "0081"
        received = solution(s)
        expected = 11
        self.assertEqual(received, expected)

    def test_3(self):
        s = "022"
        received = solution(s)
        expected = 9
        self.assertEqual(received, expected)


if __name__ == "__main__":
    unittest.main()
