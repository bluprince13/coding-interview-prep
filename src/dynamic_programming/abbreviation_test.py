# https://www.hackerrank.com/challenges/abbr

import unittest
from functools import cache
import sys

sys.setrecursionlimit(4000)

# This approach doesn't work for all cases because it assumes that if a letter
# in 'a' can be capitalized to match with the corresponding letter in 'b', then
# it should be capitalized. However, in reality, we may still be able to remove
# the letter if there's a subsequent capitalized version in 'a'. i.e. the
# problem branches.
def abbreviation_attempt1(a, b):
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
            j += 1
        elif a[i].upper() == b[j] and a[i]:
            i += 1
            j += 1
        elif a[i].islower() and a[i]:
            i += 1
        else:
            return "NO"

        # Remaining letters in 'a' cannot be less than in 'b'
        if len(a) - i < len(b) - j:
            return "NO"

    # Process remaining letters in 'a'
    while i < len(a):
        if a[i].islower():
            i += 1
        else:
            return "NO"

    return "YES"


@cache
def is_abbreviation(a, b):
    # '' == ''
    if a == "" and b == "":
        return True
    # 'Y' < 'XY'
    elif len(a) < len(b):
        return False

    a_last_letter = a[-1]
    b_last_letter = b[-1] if len(b) > 0 else None

    # X == X
    if a_last_letter == b_last_letter:
        return is_abbreviation(a[:-1], b[:-1])
    # x == X
    elif a_last_letter.upper() == b_last_letter:
        return is_abbreviation(a[:-1], b[:-1]) or is_abbreviation(a[:-1], b)
    # x != Y
    elif a_last_letter.islower():
        return is_abbreviation(a[:-1], b)
    # X != Y
    else:
        return False


def abbreviation(a, b):
    if is_abbreviation(a, b):
        return "YES"
    else:
        return "NO"


class AbbreviationAttempt1(unittest.TestCase):
    def test_trailing_small_letters_in_a(self):
        a = "daBcde"
        b = "ABC"
        received = abbreviation_attempt1(a, b)
        expected = "YES"
        self.assertEqual(received, expected)

    def test_trailing_small_letter_in_a_whose_capital_exists_in_b(self):
        a = "daBcb"
        b = "ABC"
        received = abbreviation_attempt1(a, b)
        expected = "YES"
        self.assertEqual(received, expected)

    def test_trailing_small_letters_in_a_that_were_capitalised(self):
        a = "daBcda"
        b = "ABC"
        received = abbreviation_attempt1(a, b)
        expected = "YES"
        self.assertEqual(received, expected)

    def test_trailing_capital_letters_in_a(self):
        a = "daBcdA"
        b = "ABC"
        received = abbreviation_attempt1(a, b)
        expected = "NO"
        self.assertEqual(received, expected)

    def test_trailing_letters_in_b(self):
        a = "AfPZN"
        b = "APZNC"
        received = abbreviation_attempt1(a, b)
        expected = "NO"
        self.assertEqual(received, expected)


class AbbreviationAttempt2(unittest.TestCase):
    def test_trailing_small_letters_in_a(self):
        a = "daBcde"
        b = "ABC"
        received = abbreviation(a, b)
        expected = "YES"
        self.assertEqual(received, expected)

    def test_trailing_small_letter_in_a_whose_capital_exists_in_b(self):
        a = "daBcb"
        b = "ABC"
        received = abbreviation(a, b)
        expected = "YES"
        self.assertEqual(received, expected)

    def test_trailing_small_letters_in_a_that_were_capitalised(self):
        a = "daBcda"
        b = "ABC"
        received = abbreviation(a, b)
        expected = "YES"
        self.assertEqual(received, expected)

    def test_trailing_capital_letters_in_a(self):
        a = "daBcdA"
        b = "ABC"
        received = abbreviation(a, b)
        expected = "NO"
        self.assertEqual(received, expected)

    def test_trailing_letters_in_b(self):
        a = "AfPZN"
        b = "APZNC"
        received = abbreviation(a, b)
        expected = "NO"
        self.assertEqual(received, expected)

    def test_performance(self):
        a = "OKXAJYPrZKNRQCLFKXJPJBXAEHYKXLIEIHLQYZPUNGELNKOZHsVLCPCXYSBURPRAWBAXBZBFBhCWBRNsTUNZIKriNYYPFXRNODZPCKNTTPCCZqvajmjtgxjjeafposdovrrzhkwesukvmlwbdzzlvvzyigpfvrhytcxpmbdytlkfzvnjnddpxxotsjfeuxdvmihwadpigjejtuyyrocbtlklkbsndmrpmekreqbbbznnyayzhvyjwlfqmxperliiforxddhwvectqoryxgvomhtjgizwdokbkrsbohupmkwcleetukcivqdbedyajoyglnaqzicuikmrjclfokypugvfgdfbdwpnccztmxwnyxdqrccrgoajwpyeeooesjvluyqdygiovqsrpudcjpriirnophewxcejanrbuqndxikaudmcaynpqmqpbhxwmfwuwwbvalglktmbbnleagsncvqgyduqclvnipxjkctqzatziewlccbyrukvnwuamahovdouwakuokwucexhmqvsilmsjgkqqwenmnxcyvjwjwqmflcpsjdjvagreajsmqjnpqjombmrhnvexfjsldjvapitqyajbypzqbrkladxfqiwsbwbm"
        b = "OKXAJYPZKNRQCLFKXJPJBXAEHYKXLIEIHLQYZPUNGELNKOZHVLCPCXYSBURPRAWBAXBZBFBCWBRNTUNZIKNYYPFXRNODZPCKNTTPCCZ"
        received = abbreviation(a, b)
        expected = "YES"
        self.assertEqual(received, expected)


if __name__ == "__main__":
    unittest.main()
