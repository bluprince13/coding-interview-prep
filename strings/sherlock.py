# https://www.hackerrank.com/challenges/alternating-characters/problem


# TODO: this doesn't seem very neat!
def isValid(s):
    letter_map = {}
    for letter in s:
        if letter in letter_map:
            letter_map[letter] += 1
        else:
            letter_map[letter] = 1
    freq_map = {}
    for letter, frequency in letter_map.items():
        if frequency not in freq_map:
            freq_map[frequency] = [letter]
        else:
            freq_map[frequency].append(letter)

    frequencies = list(freq_map.keys())
    no_of_letters_per_frequency = [len(letters) for letters in freq_map.values()]
    result = "NO"
    if len(frequencies) == 1:
        result = "YES"
    elif len(frequencies) == 2:
        frequency_diff = abs(frequencies[1] - frequencies[0])
        if min(no_of_letters_per_frequency) == 1:
            if frequency_diff == 1:
                result = "YES"
            elif min(frequencies) == 1:
                if len(freq_map[1]) == 1:
                    result = "YES"

    print(result)
    return result


import unittest


class MyTest(unittest.TestCase):
    def test_1(self):
        s = "aabbccddeefghi"
        received = isValid(s)
        expected = "NO"
        self.assertEqual(received, expected)

    def test_2(self):
        s = "abcdefghhgfedecba"
        received = isValid(s)
        expected = "YES"
        self.assertEqual(received, expected)

    def test_3(self):
        s = "aaaabbcc"
        received = isValid(s)
        expected = "NO"
        self.assertEqual(received, expected)

    def test_4(self):
        s = "abbbccc"
        received = isValid(s)
        expected = "YES"
        self.assertEqual(received, expected)

    def test_5(self):
        s = "aaaaabc"
        received = isValid(s)
        expected = "NO"
        self.assertEqual(received, expected)

    def test_6(self):
        s = "aabbcd"
        received = isValid(s)
        expected = "NO"
        self.assertEqual(received, expected)

if __name__ == '__main__':
    unittest.main()
