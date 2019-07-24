# no link available
# scrub HTML - remove all scripts

import unittest


def scrub(text):
    # look for the first set of script tags, remove them, repeat
    result = text
    while True:
        start_index = result.find("<script")
        stop_index = result.find("</script>") + 8

        if start_index >= 0:
            result = remove_substring(result, start_index, stop_index)
        else:
            break
    return result


def remove_substring(string, start_index, stop_index):
    # making this a separate function for readability and for a unit test
    return string[:start_index] + string[stop_index + 1:]


class MyTest(unittest.TestCase):
    def test_simple(self):
        text = """blah blah<script>
blah blah
</script>blah
blah"""
        received = scrub(text)
        expected = """blah blahblah
blah"""
        self.assertEqual(received, expected)

    def test_complex(self):
        text = """blah<script></script>
blah<script></script>"""
        received = scrub(text)
        expected = """blah
blah"""
        self.assertEqual(received, expected)

    def test_remove_substring(self):
        string = """blah star blah star blah"""
        start_index = 5
        stop_index = 8
        received = remove_substring(string, start_index, stop_index)
        expected = """blah  blah star blah"""
        self.assertEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
