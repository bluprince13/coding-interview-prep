# https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem

# SAMPLE INPUT
# 2  	- Number of queries
# 4 2 	- Number of nodes, number of edges
# 1 2 	- Node 1 connected to node 2
# 1 3	- Node 2 connected to node 3
# 1	- Start node
# 3 1
# 2 3
# 2

import unittest
from collections import defaultdict


class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        for i in range(n):
            self.graph[n]

    def connect(self, x, y):
        self.graph[x].append(y)
        self.graph[y].append(x)

    def find_all_distances(self, root):
        # Breadth First Search [BFS]
        # For each node, first the node is visited and then its child nodes are put in a FIFO queue.
        # Similar to Breadth First Traversal of a tree, but, have to keep track of visited nodes in order to avoid cycles.

        visited = [False] * self.n
        queue = []
        queue.append(root)
        visited[root] = True
        distances = [-1] * self.n
        distances[root] = 0

        while queue:
            node = queue.pop(0)
            parentDistance = distances[node]
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for child in self.graph[node]:
                if visited[child] == False:
                    distances[child] = parentDistance + 6
                    queue.append(child)
                    visited[child] = True

        distances.pop(root)
        print(" ".join)
        return distances


class MyTest(unittest.TestCase):
    def setUp(self):
        G = Graph(4)
        G.connect(0, 1)
        G.connect(0, 2)
        self.G = G

    def test_find_all_distances(self):
        received = self.G.find_all_distances(0)
        expected = [6, 6, -1]
        self.assertEqual(received, expected)


if __name__ == "__main__":
    unittest.main()
