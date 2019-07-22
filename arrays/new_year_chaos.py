# http://hr.gs/fccdad

import unittest

def minimumBribes(q):

    # let's look at the example 
    #   1   2   3   4   5
    #   2   1   5   3   4
    # advances - how much forward has each person come? 
    #   -1  1   -1  -1  2   
    # swaps visualised:
    #               x   x
    #           x   x
    #   x   x           

    # we could find the advances and add positive numbers

    # harder example
    #   1   2   3   4   5   6   7   8
    #   1   2   5   3   7   8   6   4
    # advances:
    #   0   0   -1  -4  2   -1  2   2
    # doesn't work because 6 does make x1 advance even though it ends up worse off
    # swaps visualised:
    #   1   2   3   4   5   6   7   8
    #                   x        
    #   1   2   3   5   4   6   7   8               
    #               x   
    #   1   2   5   3   4   6   7   8  
    #                           x 
    #   1   2   5   3   4   7   6   8
    #                       x
    #   1   2   5   3   7   4   6   8
    #                               x
    #   1   2   5   3   7   4   8   6
    #                           x        
    #   1   2   5   3   7   8   4   6
    #                               x
    #   1   2   5   3   7   8   6   4    
    # let's look at the problem again
    #   1   2   3   4   5   6   7   8
    #   1   2   5   3   7   8   6   4 
    # how many bribes received?
    #   0   0   1   4   0   2   0   0
    # we calc above by counting number of bigger numbers now in front of each number

    result = 0
    for index, old_position in enumerate(q):
        new_position = index + 1
        jump = old_position - new_position
        if jump > 2:
            result = "Too chaotic"
            break

        start = max(old_position - 1, 1)
        stop = new_position - 1
        for position in range(start, stop + 1):
            if q[position - 1] > old_position:
                result += 1
    
    print(result)
    return result

class MyTest(unittest.TestCase):
    def test_1(self):
        q = [2, 1, 5, 3, 4]
        expected = 3
        self.assertEqual(minimumBribes(q), expected)

    def test_2(self):
        q = [2, 5, 1, 3, 4]
        expected = "Too chaotic"
        self.assertEqual(minimumBribes(q), expected)

    def test_3(self):
        q = [1, 2, 5, 3, 7, 8, 6, 4]
        expected = 7
        self.assertEqual(minimumBribes(q), expected)

if __name__ == '__main__':
    unittest.main()