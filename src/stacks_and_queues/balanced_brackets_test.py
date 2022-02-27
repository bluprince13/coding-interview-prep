# https://www.hackerrank.com/challenges/balanced-brackets

import unittest

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# Time complexity - O(n)
# Space complexity - O(n)

# https://youtu.be/IhJGJG-9Dx8
def isBalanced(s):
    stack = []
    openBrackets = "({["
    closedBrackets = ")}]"

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
                return "NO"
        else:
            # if the stack is empty and the character is a closing bracket
            return "NO"

    # check if the stack has open brackets left
    if stack:
        return "NO"
    else:
        return "YES"


class MyTest(unittest.TestCase):
    def test_1(self):
        text = "{[()]}"
        received = isBalanced(text)
        expected = "YES"
        self.assertEqual(received, expected)

    def test_2(self):
        text = "{[(])}"
        received = isBalanced(text)
        expected = "NO"
        self.assertEqual(received, expected)

    def test_3(self):
        text = "{{[[(())]]}}"
        received = isBalanced(text)
        expected = "YES"
        self.assertEqual(received, expected)


if __name__ == "__main__":
    unittest.main()
