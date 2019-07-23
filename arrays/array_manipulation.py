# https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

# Sample Input
# 5 3
# 1 2 100
# 2 5 100
# 3 4 100

# Sample Output
# 200

def arrayManipulation(n, queries):
    gradients = [0] * n
    
    for query in queries:
        start, end, number = tuple(query)
        start -= 1
        end -= 1

        gradients[start] += number
        if end != n - 1:
            gradients[end + 1] -= number

    counter = 0
    maximum = 0
    for gradient in gradients:
        counter += gradient
        if counter > maximum:
            maximum = counter

    return maximum

import unittest

class MyTest(unittest.TestCase):
    def test_1(self):
        n = 5
        queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
        expected = 200
        self.assertEqual(arrayManipulation(n, queries), expected)

    def test_2(self):
        n = 10
        queries = [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]]
        expected = 31
        self.assertEqual(arrayManipulation(n, queries), expected)

if __name__ == '__main__':
    unittest.main()