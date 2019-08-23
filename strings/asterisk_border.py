# no link available

# draw an asterisk border around a word

import unittest


def apply_border(text):
    length = len(text)
    border = "* " * length + "*"
    if length % 2:
        text = "* " + text + " *"
    else:
        text = "* " + text + "  *"
    return "\n".join([border, text, border])


class MyTest(unittest.TestCase):
    def test_odd(self):
        text = "bla"
        received = apply_border(text)
        expected = """* * * *
* bla *
* * * *"""
        self.assertEqual(received, expected)

    def test_even(self):
        text = "blah"
        received = apply_border(text)
        expected = """* * * * *
* blah  *
* * * * *"""
        self.assertEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
