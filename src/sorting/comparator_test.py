# https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem

import unittest
from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return "%s %s" % (self.name, self.score)

    @staticmethod
    def comparator(a, b):
        if a.score > b.score:
            return -1
        elif a.score < b.score:
            return 1
        elif a.name < b.name:
            return -1
        elif a.name > b.name:
            return 1
        else:
            return 0


def get_players(a):
    data = []
    for name, score in a:
        player = Player(name, score)
        data.append(player)
    return data


def sort_players(a):
    data = get_players(a)
    data.sort(key=cmp_to_key(Player.comparator))
    return data


class MyTest(unittest.TestCase):
    def test_1(self):
        a = [('amy', 100), ('david', 100), ('heraldo', 50),
             ('aakansha', 75), ('aleksa', 150)]
        received = sort_players(a)
        a = [('aleksa', 150), ('amy', 100), ('david', 100),
             ('aakansha', 75), ('heraldo', 50)]
        expected = get_players(a)
        self.assertEqual(str(received), str(expected))


if __name__ == '__main__':
    unittest.main()
