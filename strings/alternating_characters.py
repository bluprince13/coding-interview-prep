# https://www.hackerrank.com/challenges/alternating-characters/problem

def alternatingCharacters(s):
    prev_letter = ""
    counter = 0 
    for letter in s:
        if letter == prev_letter:
            counter += 1
        prev_letter = letter
    print(counter)
    return counter

import unittest

class MyTest(unittest.TestCase):
    def test_1(self):
        s = "AAAA"
        received = alternatingCharacters(s)
        expected = 3
        self.assertEqual(received, expected)

if __name__ == '__main__':
    unittest.main()