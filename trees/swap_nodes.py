# https://www.hackerrank.com/challenges/swap-nodes-algo/

import unittest

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#


def swapNodes(indexes, queries):
    output = []
    for query in queries:
        output.append(swap(indexes, query))


def swap(indexes, query):
    print()


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def parse(indexes, root=1):
    children = indexes[0]
    left = parse([], children[0])
    right = parse([], children[1])
    return Node(root, left, right)


# Input = [[2, 3], [-1, -1], [-1, -1]]

# Swap the indices

# Output = [[3, 2], [-1, -1], [-1, -1]]

# 3 1 2 - read(x)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write("\n".join([" ".join(map(str, x)) for x in result]))
    fptr.write("\n")

    fptr.close()


class MyTest(unittest.TestCase):
    def test_1(self):
        indexes = [[2, 3], [-1, -1], [-1, -1]]
        queries = [1, 1]
        received = swapNodes(indexes, queries)
        expected = [[3, 1, 2], [2, 1, 3]]
        self.assertEqual(received, expected)


if __name__ == "__main__":
    unittest.main()
