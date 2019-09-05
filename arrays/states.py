# no link available

# Eight cells are arranged in a straight line. An integer value of 1 represents
# an active cell and a value of 0 represents an inactive cell. If neighbours
# on both sides of a cell are either active or inactive, the cell becomes
# inactive on the next day; otherwise the cell becomes active. The two cells on
# each end have a single adjacent cell, so assume that the unoccupied space on
# the opposide side is an inactie cell. The state information of all cells
# should be updated simultaneously.

import unittest


def cellCompete(states, days):
    current_states = states
    for day in range(days):
        next_states = []
        for idx, state in enumerate(current_states):
            if idx == 0:
                left = 0
            else:
                left = current_states[idx - 1]

            if idx == 7:
                right = 0
            else:
                right = current_states[idx + 1]

            if left == right:
                next_states.append(0)
            else:
                next_states.append(1)
        current_states = next_states
    return next_states


class MyTest(unittest.TestCase):
    def test_1(self):
        states = [1, 0, 0, 0, 0, 1, 0, 0]
        days = 1
        received = cellCompete(states, days)
        expected = [0, 1, 0, 0, 1, 0, 1, 0]
        self.assertSequenceEqual(received, expected)

    def test_2(self):
        states = [1, 1, 1, 0, 1, 1, 1, 1]
        days = 2
        received = cellCompete(states, days)
        expected = [0, 0, 0, 0, 0, 1, 1, 0]
        self.assertSequenceEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
