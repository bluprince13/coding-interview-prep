# How to run tests if no testing package is provided?


def add(x, y):
    return x + y


def test(args, expecteds):
    for (x, y), expected in zip(args, expecteds):
        print(add(x, y) == expected)


args = [
    (1, 1),
    (1, 2),
]

expecteds = [2, 2]

if __name__ == "__main__":
    test(args, expecteds)
