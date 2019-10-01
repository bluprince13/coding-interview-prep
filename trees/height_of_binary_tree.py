# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem

import unittest


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def height(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 0
    else:
        max_height_left = height(root.left)
        max_height_right = height(root.right)
        max_height = max(max_height_left, max_height_right)
        return max_height + 1


def get_root(arr):
    tree = BinarySearchTree()
    for i in arr:
        tree.create(i)
    return tree.root


class MyTest(unittest.TestCase):
    def test_1(self):
        arr = [3, 5, 2, 1, 4, 6, 7]
        root = get_root(arr)
        received = height(root)
        expected = 3
        self.assertEqual(received, expected)

    def test_2(self):
        arr = [15]
        root = get_root(arr)
        received = height(root)
        expected = 0
        self.assertEqual(received, expected)

    def test_3(self):
        arr = [3, 1, 7, 5, 4]
        root = get_root(arr)
        received = height(root)
        expected = 3
        self.assertEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
