# https://www.janestreet.com/puzzles/triads/

import unittest


def create_triangle(n):
    triangle = []
    for row in range(n):
        output_row = []
        for column in range(row+1):
            output_row.append(column + 1)
        triangle.append(output_row)
    return triangle


def print_triangle(triangle):
    n = len(triangle)
    for i, row in enumerate(triangle):
        output = []
        output.append(" " * ((n-i)*2))
        for column in row:
            output.append(str(column))
        print("   ".join(output))


def is_div_by_3(number):
    return number % 3 == 0


def is_triadic(n):
    state = create_triangle(n)
    for i, row in enumerate(state[:-1]):
        for j, column in enumerate(row):
            if state[i][j]:
                state[i][j] = 0
                # if not the 3rd last row or the 1st row
                if i != n - 3 or i == 0:
                    # start with upside down triangle in some cases
                    # this is kind of complex
                    if is_div_by_3(i-j+1) and j != 0 and i != j and i != n-2 and state[i+1][j-1]:
                        state = draw_upside_down_triad(state, i, j)
                    # normal triangle possible?
                    elif state[i+1][j] and state[i+1][j+1]:
                        state = draw_normal_triad(state, i, j)
                    # upside down triangle possible?
                    elif state[i][j+1] and state[i+1][j+1]:
                        state = draw_upside_down_triad(state, i, j)
                # if 3rd last row
                else:
                    # it's the last point in the row and it's not the last row
                    if i == j and i != n - 1:
                        state = draw_normal_triad(state, i, j)
                    # upside down triangle possible?
                    elif state[i][j+1] and state[i+1][j+1]:
                        state = draw_upside_down_triad(state, i, j, False)
                    else:
                        return False, state
            else:
                continue
            # print("row ", i)
            # print("column ", j)
            # print_triangle(state)
    if state[n-1][n-1]:
        return False, state
    else:
        return True, state


def draw_normal_triad(state, i, j):
    state[i+1][j] = 0
    state[i+1][j+1] = 0
    return state


def draw_upside_down_triad(state, i, j, value=0):
    state[i][j+1] = 0
    state[i+1][j+1] = 0
    return state


class MyTest(unittest.TestCase):
    def test_1(self):
        n = 2
        received = is_triadic(n)
        expected = True, [[0], [0, 0]]
        self.assertEqual(received, expected)

    def test_3(self):
        n = 3
        received = is_triadic(n)
        expected = False, [[0], [0, 0], [1, 2, 3]]
        self.assertEqual(received, expected)

    def test_4(self):
        n = 4
        received = is_triadic(n)
        expected = False, [[0], [0, 0], [0, 0, 0], [0, 0, 0, 4]]
        self.assertEqual(received, expected)

    def test_5(self):
        n = 5
        received = is_triadic(n)
        expected = False, [[0], [0, 0], [0, 0, 0],
                           [0, 0, 0, 0], [0, 0, 3, 4, 5]]
        self.assertEqual(received, expected)

    def test_6(self):
        n = 6
        received = is_triadic(n)
        expected = False, [[0], [0, 0], [0, 0, 0], [
            0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 4, 5, 6]]
        self.assertEqual(received, expected)

    def test_7(self):
        n = 7
        received = is_triadic(n)
        expected = False, [[0], [0, 0], [0, 0, 0], [
            0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7]]
        self.assertEqual(received, expected)

    def test_8(self):
        n = 8
        received = is_triadic(n)
        expected = False, [[0], [0, 0], [0, 0, 0], [
            0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 6, 7, 8]]
        self.assertEqual(received, expected)

    def test_9(self):
        n = 9
        received = is_triadic(n)
        expected = True
        self.assertEqual(received[0], expected)

    def test_10(self):
        n = 10
        received = is_triadic(n)
        expected = False
        self.assertEqual(received[0], expected)

    def test_11(self):
        n = 11
        received = is_triadic(n)
        expected = True
        self.assertEqual(received[0], expected)

    def test_12(self):
        n = 12
        received = is_triadic(n)
        expected = True
        self.assertEqual(received[0], expected)

    def test_13(self):
        n = 13
        received = is_triadic(n)
        expected = False
        self.assertEqual(received[0], expected)

    def test_14(self):
        n = 14
        received = is_triadic(n)
        expected = True
        self.assertEqual(received[0], expected)

    def test_15(self):
        n = 15
        received = is_triadic(n)
        expected = False
        self.assertEqual(received[0], expected)


if __name__ == '__main__':
    sumofn = 0
    for n in range(2, 40):
        satisfied = is_triadic(n)[0]
        if satisfied:
            print("n = ", n, " - Y")
            sumofn += n
        else:
            print("n = ", n, " - N")
    print("Sum of n: ", sumofn)

    unittest.main()
