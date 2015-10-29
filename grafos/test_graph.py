#
# Everaldo Gomes - everaldo.gomes@pucpr.br
# 28/10/2015
#
#


import unittest

from vertex import Vertex
from edge import Edge
from graph import Graph
from edges import Edges
from vertices import Vertices

class TestGraph(unittest.TestCase):


    def setUp(self):
        self.a = Vertex('a')
        self.b = Vertex('b')
        self.c = Vertex('c')
        self.d = Vertex('d')
        self.e1 = Edge(self.a, self.b)
        self.e2 = Edge(self.a, self.d)
        self.e3 = Edge(self.c, self.d)
        self.e4 = Edge(self.b, self.d)
        self.edges = Edges({self.e1, self.e2, self.e3, self.e4})
        self.vertices = Vertices({self.a, self.b, self.c, self.d})
        self.g = Graph(self.vertices, self.edges)

    def test_adjacency_list(self):
        self.assertEqual(self.g.adjacency, \
            {self.a: {self.b, self.d},
             self.b: {self.a, self.d},
             self.c: {self.d},
             self.d: {self.a, self.b, self.c}})

    def test_incidence_matrix(self):
        self.g.incidence_matrix()
        m = self.g.i_matrix
        for edge in self.g.edges:
            u, v = edge.e
            self.assertTrue(m.adjacent(u, v))

    def test_min_degree(self):
        self.assertEqual(self.g.min_degree(), 1)

    def test_max_degree(self):
        self.assertEqual(self.g.max_degree(), 3)


    def test_complement_graph(self):
        c = self.g.complement()
        self.assertEqual(c.vertices, self.g.vertices)



if __name__ == '__main__':
    unittest.main(verbosity=2)

