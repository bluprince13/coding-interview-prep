# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

def makeAnagram(a, b):
    # example 1:
    #   cde, abc
    #   c is in abc
    #   d not in ab => 1
    #   e not in ab => 1
    #   ab not in cde => 2
    #   answer is 1 + 1 + 2 = 4!
    temp_b = b
    counter = 0

    for letter in a:
        if letter in temp_b:
            temp_b = temp_b.replace(letter, "", 1)
        else:
            counter += 1
    
    result = counter + len(temp_b)
    print(result)
    return result 
             
import unittest

class MyTest(unittest.TestCase):
    def test_1(self):
        a = "cde"
        b = "abc"
        received = makeAnagram(a, b)
        expected = 4
        self.assertEqual(received, expected)

if __name__ == '__main__':
    unittest.main()