# no link available

# draw an asterisk border around a word

import unittest


def apply_border(text):
    length = len(text)
    border = "* " + "* " * (int(length/2) + 1) + "*"

    if length % 2:
        text = "* " + text + " *"
    else:
        text = "* " + text + "  *"
    return "\n".join([border, text, border])


class MyTest(unittest.TestCase):
    def test_3(self):
        text = "abc"
        received = apply_border(text)
        expected = """* * * *
* abc *
* * * *"""
        self.assertEqual(received, expected)

    def test_4(self):
        text = "abcd"
        received = apply_border(text)
        expected = """* * * * *
* abcd  *
* * * * *"""
        self.assertEqual(received, expected)

    def test_5(self):
        text = "abcde"
        received = apply_border(text)
        expected = """* * * * *
* abcde *
* * * * *"""
        self.assertEqual(received, expected)

    def test_6(self):
        text = "abcdef"
        received = apply_border(text)
        expected = """* * * * * *
* abcdef  *
* * * * * *"""
        self.assertEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
