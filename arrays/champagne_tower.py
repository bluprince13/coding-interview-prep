# https://leetcode.com/problems/champagne-tower/

import unittest

def pour_value(cups, row, glass):

    result = [[cups]]

    for curr_row in range(row + 1):
        num_glasses = curr_row + 1
        next_row = curr_row + 1
        next_row_contents = [0 for _ in range(next_row + 1)]
        result.append(next_row_contents)

        for curr_glass in range(num_glasses):
            curr_value = result[curr_row][curr_glass]
            
            if curr_value > 1:
                new_value = 1
                spillage = (curr_value - 1) / 2

                result[curr_row][curr_glass] = new_value
                result[next_row][curr_glass] += spillage
                result[next_row][curr_glass + 1] += spillage
    
    return result, result[row][glass]

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(pour_value(4, 1, 1), ([[1], [1, 1], [0.25, 0.5, 0.25]], 1))

if __name__ == '__main__':
    unittest.main()