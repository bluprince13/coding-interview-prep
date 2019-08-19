# no link available
# A and B are two matrices
# A is 52 x 4000
# B is n x 2
# first col of B
#   B(1,1) = A(1,1)
#   B(2,1) = A(2,1)
#   B(52,1) = A(52,1)
#   B(53,1) = A(1,1)
#   B(54,1) = A(2,1)
#   ...
#   B(n,1) = A(52,1)
# second col of B
#   B(1,2) = A(1,2)
#   B(2,2) = A(2,2)
#   B(52,2) = A(52,2)
#   B(53,2) = A(1,3)
#   B(54,2) = A(2,3)
#   ...
#   B(n,2) = A(52,4000)
# given A, find B


# Let's make this more general by saying A is i x j

import numpy as np
import unittest


def getB(A):
    # first identify shape of the matrix
    i, j = A.shape
    # then define num_sets which we will use later
    num_sets = j - 1

    # to find the first col of B, we identify the first col of A
    b_col1 = A[:, 0]
    # and repeat it num_sets times
    b_col1 = np.tile(b_col1, num_sets)

    # to find the second col of B, we start by flattening A
    b_col2 = A.flatten(order='F')
    # and then remove the first i elements
    b_col2 = b_col2[i:]

    # finally, stack the first and second columns of B together
    B = np.column_stack((b_col1, b_col2))
    return B


class MyTest(unittest.TestCase):
    def test_1(self):
        A = np.array([[1, 2], [3, 4]])
        received = getB(A).tolist()
        expected = A.tolist()
        self.assertSequenceEqual(received, expected)

    def test_2(self):
        A = np.array([[1, 2, 3], [4, 5, 6]])
        received = getB(A).tolist()
        expected = np.array([[1, 2], [4, 5], [1, 3], [4, 6]]).tolist()
        self.assertSequenceEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
