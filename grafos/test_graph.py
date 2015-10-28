#
# Everaldo Gomes - everaldo.gomes@pucpr.br
# 28/10/2015
#
#


import unittest

from vertex import Vertex
from edge import Edge
from graph import Graph

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
        self.edges = {self.e1, self.e2, self.e3, self.e4}
        self.g = Graph({self.a, self.b, self.c, self.d}, self.edges)

    def test_adjacency_list(self):
        self.assertEqual(self.g.adjacency, \
            {self.a: {self.b, self.d},
             self.b: {self.a, self.d},
             self.c: {self.d},
             self.d: {self.a, self.b, self.c}})



if __name__ == '__main__':
    unittest.main(verbosity=2)

