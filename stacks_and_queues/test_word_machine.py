# Zalando online assessment - 66%

import unittest


def parse(s):
    split = s.split(" ")
    result = []
    for x in split:
        if x.isnumeric():
            result.append(int(x))
        else:
            result.append(x)
    return result


def wordMachine(s):
    words = parse(s)
    stack = []
    operations = ["+", "-", "POP", "DUP"]

    for word in words:
        if word not in operations:
            stack.append(word)
        elif word == "+":
            if len(stack) < 2:
                return -1
            stack.append(stack.pop() + stack.pop())
        elif word == "-":
            if len(stack) < 2:
                return -1
            stack.append(stack.pop() - stack.pop())
        elif word == "DUP":
            if len(stack) < 1:
                return -1
            stack.append(stack[-1])
        elif word == "POP":
            if len(stack) < 1:
                return -1
            stack.pop()

        if stack[-1] > 1048575 or stack[-1] < 0:
            return -1

    if not stack:
        return -1

    return stack[-1]


class MyTest(unittest.TestCase):
    def test_1(self):
        s = "4 5 6 - 7 +"
        received = wordMachine(s)
        expected = 8
        self.assertEqual(received, expected)

    def test_2(self):
        s = "13 DUP 4 POP 5 DUP + DUP + -"
        received = wordMachine(s)
        expected = 7
        self.assertEqual(received, expected)

    def test_3(self):
        s = "5 6 + -"
        received = wordMachine(s)
        expected = -1
        self.assertEqual(received, expected)

    def test_4(self):
        s = "3 DUP 5 - -"
        received = wordMachine(s)
        expected = -1
        self.assertEqual(received, expected)

    def test_5(self):
        s = "1048575 DUP +"
        received = wordMachine(s)
        expected = -1
        self.assertEqual(received, expected)


if __name__ == "__main__":
    unittest.main()
