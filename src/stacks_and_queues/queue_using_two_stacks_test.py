# https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks

import unittest

class Stack:
    def __init__(self):
        self.list = []

    def push(self,item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()

    def peek(self):
        return self.list[-1]

    def isEmpty(self):
        return len(self.list) == 0

# https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks
class MyQueue(object):
    def __init__(self):
        self.stackNewestOnTop = Stack()
        self.stackOldestOnTop = Stack()

    def shift_stacks(self):
        if self.stackOldestOnTop.isEmpty():
            while not self.stackNewestOnTop.isEmpty():
                self.stackOldestOnTop.push(self.stackNewestOnTop.pop())

    def peek(self):
        self.shift_stacks()
        return self.stackOldestOnTop.peek()

    def pop(self):
        self.shift_stacks()
        return self.stackOldestOnTop.pop()

    def put(self, value):
        self.stackNewestOnTop.push(value)

class MyTest(unittest.TestCase):
    def setUp(self):
        Q = MyQueue()
        Q.put(0)
        Q.put(1)
        self.Q = Q

    def test_peek(self):
        received = self.Q.peek()
        expected = 0
        self.assertEqual(received, expected)

        received = self.Q.peek()
        expected = 0
        self.assertEqual(received, expected)

    def test_pop(self):
        received = self.Q.pop()
        expected = 0
        self.assertEqual(received, expected)

        received = self.Q.pop()
        expected = 1
        self.assertEqual(received, expected)

    def test_put(self):
        self.Q.put(2)
        self.Q.pop()
        self.Q.pop()
        received = self.Q.pop()
        expected = 2
        self.assertEqual(received, expected)


if __name__ == "__main__":
    unittest.main()
