# http://hr.gs/16xx

import unittest

def rotLeft(a, d):

    # don't want to do each rotation manually as that'd be O(n * d)
    # ideally O(n), so that number of rotations, d, does not matter

    # consider the example
    # [1, 2, 3, 4, 5] => [5, 1, 2, 3, 4] after 4 rotations
    # index of 5 went from 4 to 0 (which is 4 - 4)
    # index of 1 went from 0 to 1 (which is 0 - 4 + 5)

    # what if there were more rotations => very negative numbers
    # [1, 2, 3]
    # [2, 3, 1] - 1st rotation
    # [3, 1, 2] - 2nd rotation
    # [1, 2, 3] - 3rd rotation
    # [2, 3, 1] - 4th rotation
    # index of 1 went from 0 to 2 (which is 0 - 4%3 + 3 to make it non-neg)
    # index of 2 went from 1 to 0 (which is 1 - 4%3)

    result = a.copy()
    n = len(a)
    for idx, num in enumerate(a):
        new_idx = idx - (d % n)
        if new_idx < 0: 
            new_idx += n
        result[new_idx] = num
    
    return result


class MyTest(unittest.TestCase):
    def test_1(self):
        a = [1, 2, 3, 4, 5]
        d = 4
        expected = [5, 1, 2, 3, 4]
        self.assertEqual(rotLeft(a, d), expected)

if __name__ == '__main__':
    unittest.main()