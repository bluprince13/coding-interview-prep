# https://adventofcode.com/2021/day/4

import unittest
from functools import reduce


def parse_board(board):
    for row_index, row in enumerate(board):
        row = row.strip().split(" ")
        row = list(filter(bool, row))
        for number_index, number in enumerate(row):
            row[number_index] = int(number)
        board[row_index] = row
    return board


def parse(lines):
    draws = list(map(int, lines[0].split(",")))
    num_boards = (len(lines) - 1) // 6
    boards = []
    for i in range(num_boards):
        board = lines[i * 6 + 2 : i * 6 + 7]
        boards.append(parse_board(board))
    return draws, boards


def get_data(file):
    with open(file) as f:
        lines = f.read().splitlines()
    return parse(lines)


def play_draw_on_board(board, draw, counters):
    found_zero = False
    for row_index, row in enumerate(board):
        for column_index, number in enumerate(row):
            if number == draw:
                counters[0][row_index] -= 1
                counters[1][column_index] -= 1
                if counters[0][row_index] == 0 or counters[1][column_index] == 0:
                    found_zero = True
    return counters, found_zero


def get_sum_of_unmarked_numbers(draws, board):
    board_numbers = reduce(lambda a, b: a + b, board)
    unmarked_numbers = [number for number in board_numbers if number not in draws]
    return sum(unmarked_numbers)


def play_bingo(draws, boards, get_winner=True):
    counters = [([5, 5, 5, 5, 5], [5, 5, 5, 5, 5]) for _ in boards]
    players = list(range(len(boards)))
    for draw_index, draw in enumerate(draws):
        for board_index, board in enumerate(boards):
            counters[board_index], found_zero = play_draw_on_board(
                board, draw, counters[board_index]
            )
            if found_zero:
                if board_index in players:
                    players.remove(board_index)

                if get_winner:
                    return (
                        get_sum_of_unmarked_numbers(draws[: draw_index + 1], board)
                        * draw
                    )
                elif len(players) == 0:
                    return (
                        get_sum_of_unmarked_numbers(draws[: draw_index + 1], board)
                        * draw
                    )


class MyTest(unittest.TestCase):
    def test_play_bingo_get_winner(self):
        received = play_bingo(*get_data("test_input.txt"))
        expected = 4512
        self.assertEqual(received, expected)

    def test_play_bingo_get_loser(self):
        received = play_bingo(*get_data("test_input.txt"), False)
        expected = 1924
        self.assertEqual(received, expected)


if __name__ == "__main__":
    # unittest.main()

    draws, boards = get_data("input.txt")
    part1 = play_bingo(draws, boards)
    part2 = play_bingo(draws, boards, False)
    print(part1)
    print(part2)
