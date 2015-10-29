#
# Everaldo Gomes - everaldo.gomes@pucpr.br
# 28/10/2015
#
#


import unittest

from vertex import Vertex
from vertices import Vertices
from edge import Edge
from neighbors import Neighbors


class TestNeighbors(unittest.TestCase):


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

    def test_neighbors(self):
        n_a = Neighbors.get(self.a, self.edges)
        n_b = Neighbors.get(self.b, self.edges)
        n_c = Neighbors.get(self.c, self.edges)
        n_d = Neighbors.get(self.d, self.edges)
        self.assertTrue(Vertices({self.b, self.d}) == n_a)
        self.assertTrue(Vertices({self.a, self.c}).isdisjoint(n_a))
        self.assertTrue(Vertices({self.a, self.d}) == n_b)
        self.assertTrue(Vertices({self.b, self.c}).isdisjoint(n_b))
        self.assertTrue(Vertices({self.d}) == n_c)
        self.assertTrue(Vertices({self.a, self.b, self.c}).isdisjoint(n_c))
        self.assertTrue(Vertices({self.a, self.b, self.c}) == n_d)
        self.assertTrue(Vertices({self.d}).isdisjoint(n_d))




if __name__ == '__main__':
    unittest.main(verbosity=2)

