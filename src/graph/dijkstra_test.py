# https://www.hackerrank.com/challenges/dijkstrashortreach

import unittest
import sys
import collections

# https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    """
    This method makes sure that the graph is symmetrical. In other words, if there's a path from node A to B with a weight V, there needs to be a path from node B to node A with a weight V.
    """

    def construct_graph(self, nodes, init_graph):
        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph)

        for node, edges in graph.items():
            for adjacent_node, weight in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = weight

        return graph

    def get_nodes(self):
        return self.nodes

    def get_outgoing_edges(self, node):
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

    def get_weight(self, node1, node2):
        return self.graph[node1][node2]


def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())

    # the best-known cost of visiting a node from the
    # start_node. Initially, set to infinity for all nodes.
    shortest_path = {}
    # the trajectory of the current best known path for each node
    previous_nodes = {}

    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    shortest_path[start_node] = 0

    while unvisited_nodes:

        # find the node with the lowest value
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        # retrieve the current node's neighbors and update their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.get_weight(
                current_min_node, neighbor
            )
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_nodes[neighbor] = current_min_node

        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path


# https://www.hackerrank.com/challenges/dijkstrashortreach/
# TODO: This fails a lot of the tests, so something needs fixing
def shortestReach(n, edges, s):
    nodes = list(range(1, n + 1))
    init_graph = collections.defaultdict(dict)
    for start_node, end_node, weight in edges:
        if end_node in init_graph[start_node]:
            if weight < init_graph[start_node][end_node]:
                init_graph[start_node][end_node] = weight
        else:
            init_graph[start_node][end_node] = weight

    G = Graph(nodes, init_graph)
    _, shortest_path = dijkstra_algorithm(G, s)

    for node in shortest_path:
        if shortest_path[node] == sys.maxsize:
            shortest_path[node] = -1

    nodes.remove(s)
    return [shortest_path[node] for node in nodes]


class GraphTest(unittest.TestCase):
    def setUp(self):
        G = Graph([1, 2, 3], {1: {2: 10}})
        self.G = G

    def test_get_nodes(self):
        received = self.G.get_nodes()
        expected = [1, 2, 3]
        self.assertEqual(received, expected)

    def test_get_outgoing_edges(self):
        received = self.G.get_outgoing_edges(2)
        expected = [1]
        self.assertEqual(received, expected)

    def test_get_weight(self):
        received = self.G.get_weight(1, 2)
        expected = 10
        self.assertEqual(received, expected)


class MyTest(unittest.TestCase):
    def setUp(self):
        G = Graph([1, 2, 3], {1: {2: 10}})
        self.G = G

    def test_dijkstra_algorithm(self):
        received = dijkstra_algorithm(self.G, 1)
        expected = ({2: 1}, {1: 0, 2: 10, 3: sys.maxsize})
        self.assertEqual(received, expected)

    def test_shortest_reach_1(self):
        received = shortestReach(4, [[1, 2, 24], [1, 4, 20], [3, 1, 3], [4, 3, 12]], 1)
        expected = [24, 3, 15]
        self.assertEqual(received, expected)

    def test_shortest_reach_2(self):
        received = shortestReach(5, [[1, 2, 10], [1, 3, 6], [2, 4, 8]], 2)
        expected = [10, 16, 8, -1]
        self.assertEqual(received, expected)


if __name__ == "__main__":
    unittest.main()
