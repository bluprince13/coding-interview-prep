# https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem

import unittest

# LinkedList classes copied from https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def has_cycle(head):
    if head == None:
        return False
    slow = head
    fast = head.next
    while fast != None and fast.next != None:
        if fast == slow:
            return True
        slow = slow.next
        fast = fast.next.next
    return False


class MyTest(unittest.TestCase):
    def setUp(self):
        l = SinglyLinkedList()
        for i in range(5):
            l.insert_node(i)
        self.l = l

    def test_has_cycle_returns_false(self):
        received = has_cycle(self.l.head)
        expected = False
        self.assertEqual(received, expected)

    def test_has_cycle_returns_true(self):
        self.l.tail.next = self.l.head
        received = has_cycle(self.l.head)
        expected = True
        self.assertEqual(received, expected)


if __name__ == "__main__":
    unittest.main()
