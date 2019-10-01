# https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem

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


def lca(root, v1, v2):
    if root.info < v1 and root.info < v2:
        return lca(root.right, v1, v2)
    elif root.info > v1 and root.info > v2:
        return lca(root.left, v1, v2)
    else:
        return root


def get_root(arr):
    tree = BinarySearchTree()
    for i in arr:
        tree.create(i)
    return tree.root


class MyTest(unittest.TestCase):
    def test_1(self):
        arr = [4, 2, 3, 1, 7, 6]
        root = get_root(arr)
        v1, v2 = 1, 7
        received = lca(root, v1, v2).info
        expected = 4
        self.assertEqual(received, expected)

    def test_2(self):
        arr = [1, 2]
        root = get_root(arr)
        v1, v2 = 1, 2
        received = lca(root, v1, v2).info
        expected = 1
        self.assertEqual(received, expected)

    def test_3(self):
        arr = [5, 3, 8, 2, 4, 6, 7]
        root = get_root(arr)
        v1, v2 = 7, 3
        received = lca(root, v1, v2).info
        expected = 5
        self.assertEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
