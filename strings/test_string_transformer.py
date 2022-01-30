# Zalando online assessment

import unittest

remove_combos = ["AB", "BA", "CD", "DC"]


def transform_string(s):
    stack = []
    for letter in s:
        if not stack:
            stack.append(letter)
            continue
        combo = stack[-1] + letter
        if combo in remove_combos:
            stack.pop()
        else:
            stack.append(letter)
    return "".join(stack)


class MyTest(unittest.TestCase):
    def test_1(self):
        s = "CBACD"
        received = transform_string(s)
        expected = "C"
        self.assertEqual(received, expected)

    def test_2(self):
        s = "CABABD"
        received = transform_string(s)
        expected = ""
        self.assertEqual(received, expected)

    def test_3(self):
        s = "ACBDACBD"
        received = transform_string(s)
        expected = "ACBDACBD"
        self.assertEqual(received, expected)


if __name__ == "__main__":
    unittest.main()
