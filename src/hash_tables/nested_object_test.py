# no link available

import unittest


def get_value(obj, key_string):
    keys = key_string.split("/")
    value = obj
    for key in keys:
        try:
            value = value[key]
        except KeyError:
            raise Exception("%s is not there" % (key))
    return value


class MyTest(unittest.TestCase):
    def test_string(self):
        obj = {"a": {"b": {"c": "d"}}}
        key_string = "a/b/c"
        received = get_value(obj, key_string)
        expected = "d"
        self.assertEqual(received, expected)

    def test_dict(self):
        obj = {"a": {"b": {"c": "d"}}}
        key_string = "a/b"
        received = get_value(obj, key_string)
        expected = {"c": "d"}
        self.assertEqual(received, expected)

    def test_fail(self):
        obj = {"a": {"b": {"c": "d"}}}
        key_string = "a/e"
        with self.assertRaises(Exception):
            get_value(obj, key_string)


if __name__ == '__main__':
    unittest.main()
