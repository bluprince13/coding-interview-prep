import unittest
import io
import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        # TODO: Is this correct?
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def traverse_inorder(root):
    # Left - Parent - Right
    if root is None:
        return []
    return traverse_inorder(root.left) + [root.data] + traverse_inorder(root.right)


def traverse_preorder(root):
    # Parent - Left - Right
    if root is None:
        return []
    return [root.data] + traverse_preorder(root.left) + traverse_preorder(root.right)


def traverse_postorder(root):
    # Left - Right - Parent
    if root is None:
        return []
    return traverse_postorder(root.left) + traverse_postorder(root.right) + [root.data]


# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem
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


def is_isometric(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False

    return (
        is_isometric(a.left, b.left)
        and a.data == b.data
        and is_isometric(a.right, b.right)
    )


class MyTest(unittest.TestCase):
    def setUp(self):
        self.capturedOutput = io.StringIO()
        sys.stdout = self.capturedOutput

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_height_1(self):
        arr = [3, 5, 2, 1, 4, 6, 7]
        root = get_root(arr)
        received = height(root)
        expected = 3
        self.assertEqual(received, expected)

    def test_height_2(self):
        arr = [15]
        root = get_root(arr)
        received = height(root)
        expected = 0
        self.assertEqual(received, expected)

    def test_height_3(self):
        arr = [3, 1, 7, 5, 4]
        root = get_root(arr)
        received = height(root)
        expected = 3
        self.assertEqual(received, expected)

    def test_traverse_inorder(self):
        arr = [2, 1, 3]
        root = get_root(arr)
        received = traverse_inorder(root)
        expected = [1, 2, 3]
        self.assertEqual(received, expected)

    def test_traverse_preorder(self):
        arr = [2, 1, 3]
        root = get_root(arr)
        received = traverse_preorder(root)
        expected = [2, 1, 3]
        self.assertEqual(received, expected)

    def test_traverse_postorder(self):
        arr = [2, 1, 3]
        root = get_root(arr)
        received = traverse_postorder(root)
        expected = [1, 3, 2]
        self.assertEqual(received, expected)

    def test_is_isometric_true(self):
        arr = [2, 1, 3]
        a = get_root(arr)
        b = get_root(arr)
        received = is_isometric(a, b)
        expected = True
        self.assertEqual(received, expected)

    def test_is_isometric_false(self):
        a = get_root([2, 1, 3])
        b = get_root([1, 2, 3])
        received = is_isometric(a, b)
        expected = False
        self.assertEqual(received, expected)


if __name__ == "__main__":
    unittest.main()
