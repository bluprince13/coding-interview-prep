# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

import unittest

# O(n^2)

def countSwaps(a):
    tally = 0

    for i, _ in enumerate(a[:-1]):
        swapped_at_least_once = False
        # Iterate until end of unsorted part of the list
        for j, _ in enumerate(a[:-i-1]):
            if a[j] > a[j + 1]:
                tally += 1
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped_at_least_once = True

        # Exit the loop if list is already sorted
        if not swapped_at_least_once:
            break

    minimum = a[0]
    maximum = a[-1]

    print("Array is sorted in %s swaps." % (tally))
    print("First Element: %s" % (minimum))
    print("Last Element: %s" % (maximum))
    return tally, minimum, maximum


class MyTest(unittest.TestCase):
    def test_1(self):
        a = [1, 2, 3]
        received = countSwaps(a)
        expected = 0, 1, 3
        self.assertEqual(received, expected)

    def test_2(self):
        a = [3, 2, 1]
        received = countSwaps(a)
        expected = 3, 1, 3
        self.assertEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
