# Google interview 22-03

# a - (b + a) => a
# Just addition and subtraction and brackets
# No multiplication or division

# a + b + c + d + a => 2a + b + c + d
# a -(-(b + a) + a) => a + b

import unittest

# O(N) time complexity
def simplify(expression):
    store = {}
    sign = 1
    brackets_stack = [1]

    for character in expression:
        if character == " ":
            continue
        elif character == "+":
            sign = 1
        elif character == "-":
            sign = -1
        elif character == "(":
            brackets_stack.append(sign * brackets_stack[-1])
        elif character == ")":
            brackets_stack.pop()
        else:
            if character in store:
                store[character] += sign * brackets_stack[-1]
            else:
                store[character] = sign * brackets_stack[-1]

    character_list = [
        (k, v) for k, v in store.items() if v != 0
    ]  # Filter out zero terms
    character_list.sort(key=lambda x: x[0])  # Sort by key
    expression = []
    for i, (k, v) in enumerate(character_list):
        if v == 1:
            if i != 0:
                expression.append("+")
        elif v == -1:
            expression.append("-")
        else:
            expression.append(str(v))
        expression.append(k)
    return "".join(expression)


class MyTest(unittest.TestCase):
    def test_simplify(self):
        expression = "a - b + a"
        received = simplify(expression)
        expected = "2a-b"
        self.assertEqual(received, expected)

    def test_brackets(self):
        expression = "a - (b + a)"
        received = simplify(expression)
        expected = "b"
        self.assertEqual(received, expected)


if __name__ == "__main__":
    unittest.main()
