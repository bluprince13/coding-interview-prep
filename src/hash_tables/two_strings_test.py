# https://www.hackerrank.com/challenges/two-strings/problem

import unittest


def twoStrings(s1, s2):
    # example 1: hello, world
    result = "NO"
    for letter in s1:
        if letter in s2:
            result = "YES"
            break
    print(result)
    return result


class MyTest(unittest.TestCase):
    def test_1(self):
        s1 = "hello"
        s2 = "world"
        received = twoStrings(s1, s2)
        expected = "YES"
        self.assertEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
