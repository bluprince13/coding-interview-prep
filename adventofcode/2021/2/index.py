# https://adventofcode.com/2021/day/1

import unittest


def parse(lines):
    output = []
    for line in lines:
        values = line.split(" ")
        output.append(((values[0]), int(values[1])))
    return output


def get_data():
    with open("./input.txt") as f:
        lines = f.read().splitlines()
    return parse(lines)


def calculatePosition(commands):
    x = 0
    y = 0
    for command in commands:
        direction = command[0]
        distance = command[1]
        if direction == "forward":
            x += distance
        elif direction == "down":
            y += distance
        else:
            y -= distance
    return x * y

def calculatePositionV2(commands):
    x = 0
    y = 0
    aim = 0
    for command in commands:
        direction = command[0]
        distance = command[1]
        if direction == "forward":
            x += distance
            y += distance * aim
        elif direction == "down":
            aim += distance
        else:
            aim -= distance
    return x * y


class MyTest(unittest.TestCase):
    def test_1(self):
        measurements = parse(
            ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
        )
        received = calculatePosition(measurements)
        expected = 150
        self.assertEqual(received, expected)

    def test_2(self):
        measurements = parse(
            ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
        )
        received = calculatePositionV2(measurements)
        expected = 900
        self.assertEqual(received, expected)


if __name__ == "__main__":
    # unittest.main()

    commands = get_data()
    part1 = calculatePosition(commands)
    part2 = calculatePositionV2(commands)
    print(part1)
    print(part2)
