# https://www.hackerrank.com/challenges/special-palindrome-again/problem

import unittest


def substrCount(n, s):
    # example 1: aaabaaa - symmetry about one letter
    #   aba
    #   aabaa
    #   aaabaaa
    #   'symmetry_count' = 3 which is the streak after the middle
    # example 2: aaaaa - same letter
    #   aa
    #   aa, aaa
    #   aa, aaa, aaaa
    #   aa, aaa, aaaa, aaaaa
    #   'same_count' = 10 which is 1 + 2 + (streak - 2) + (streak - 1)
    # example 3: aaababbbaa - mixed
    #   aa
    #   aa, aaa
    #   aba
    #   bab
    #   bb
    #   bb, bbb
    #   aa
    #   symmetry_count => 2
    #   same_count => 7
    #   note that substrings aba and bab share two letters!!

    # same_count is fairly trivial
    # symmetry_count requires a fair bit of logic though

    streak = 1
    last_letter = ""
    same_count = 0

    passed_middle = False
    symmetry_count = 0
    previous_streak = 0

    for idx, letter in enumerate(s):
        if letter == last_letter:
            streak += 1
            same_count += streak - 1

            # symmetry_count should only be incremented when
            #   1 - we have passed the 'middle'
            #       aaaaMaaaxa - at x, we have passed the middle, M
            #       aaaxMaaaaa - at x, we have not passed the middle, M
            #   2 - we have not exceeded the previous streak
            #       aaMax - at x, we have not exceeded the previous streak of 2
            #       aaMaax - at x, we have exceeded the previous streak of 2
            if passed_middle and streak <= previous_streak:
                symmetry_count += 1
        else:
            if idx >= 2:
                last_last_letter = s[idx - 2]

                # detect a 'middle' we have just passed
                # aMx - at x == a,
                #   set the passed middle flag to true
                #   increment the counter
                # abx - at x != a,
                #   set the passed middle flag to false
                #   set the previous streak to 0
                if last_last_letter == letter:
                    passed_middle = True
                    symmetry_count += 1
                else:
                    passed_middle = False
                    previous_streak = 0

            if idx < n - 1:
                next_letter = s[idx + 1]
                # if a 'middle' is coming up, store the current streak value
                # aaxMa - at x == a, store the current streak value of 3
                if last_letter == next_letter:
                    previous_streak = streak

            # reset whenever streak is lost
            streak = 1
            last_letter = letter

    result = n + symmetry_count + same_count
    return result, symmetry_count, same_count


class MyTest(unittest.TestCase):
    def test_symmetrical(self):
        n = 7
        s = "aaabaaa"
        received = substrCount(n, s)[1]
        expected = 3
        self.assertEqual(received, expected)

    def test_same(self):
        n = 5
        s = "aaaaa"
        received = substrCount(n, s)[2]
        expected = 10
        self.assertEqual(received, expected)

    def test_mixed(self):
        n = 10
        s = "aaababbbaa"
        received = substrCount(n, s)
        expected = 19, 2, 7
        self.assertEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
