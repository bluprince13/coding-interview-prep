# https://www.hackerrank.com/challenges/common-child/problem

import unittest


def commonChild(s1, s2):
    longest_child = ''
    common_children = []
    tried_start_letters = []
    for s1_idx, start_letter in enumerate(s1):
        if start_letter in s2 and start_letter not in tried_start_letters:
            tried_start_letters.append(start_letter)
            common_child = start_letter
            s2_idx = s2.find(start_letter) + 1
            s2_remaining = s2[s2_idx:]
            for letter in s1[s1_idx+1:]:
                if letter in s2_remaining:
                    common_child = common_child + letter
                    s2_idx = s2_remaining.find(letter) + 1
                    s2_remaining = s2_remaining[s2_idx:]
            common_children.append(common_child)
            if len(common_child) > len(longest_child):
                longest_child = common_child
    print(longest_child)
    return len(longest_child)


class MyTest(unittest.TestCase):
    def test_1(self):
        s1 = "HARRY"
        s2 = "SALLY"
        received = commonChild(s1, s2)
        expected = 2
        self.assertEqual(received, expected)

    def test_2(self):
        s1 = "SHINCHAN"
        s2 = "NOHARAAA"
        received = commonChild(s1, s2)
        expected = 3
        self.assertEqual(received, expected)

    def test_3(self):
        s1 = "AABCD"
        s2 = "ABACD"
        received = commonChild(s1, s2)
        expected = 4
        self.assertEqual(received, expected)

    def test_4(self):
        s1 = "ABACD"
        s2 = "AABCD"
        received = commonChild(s1, s2)
        expected = 4
        self.assertEqual(received, expected)

    def test_5(self):
        s1 = "OUDFRMYMAW"
        s2 = "AWHYFCCMQX"
        received = commonChild(s1, s2)
        expected = 2
        self.assertEqual(received, expected)

    def test_6(self):
        # we could miss a longer child if we latch on to a smaller child
        # in the following example, ACDE is the longest child
        # to find it, we'd have to skip over B in s1!
        s1 = "ABCDE"
        s2 = "ACDEB"
        received = commonChild(s1, s2)
        expected = 4
        self.assertEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
