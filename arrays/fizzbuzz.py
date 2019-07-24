# https://www.hackerrank.com/challenges/fizzbuzz/problem

import unittest


def getFizzbuzz(N):
    # it's neater to store strings in variables
    fizz = "Fizz"
    buzz = "Buzz"
    fizz_buzz = fizz + buzz

    # this is self-explanatory
    result = []
    for i in range(1, N + 1):
        if i % 3 == 0:
            if i % 5 == 0:
                result.append(fizz_buzz)
            else:
                result.append(fizz)
        elif i % 5 == 0:
            result.append(buzz)
        else:
            result.append(i)
    for i in result:
        print(i)

    # returning a value so that it's easy to unittest
    return result


class MyTest(unittest.TestCase):
    def test_1(self):
        N = 15
        received = getFizzbuzz(N)
        expected = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
        self.assertEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
