#
# Everaldo Gomes - everaldo.gomes@pucpr.br
# 28/10/2015
#
#


import unittest

from vertex import Vertex
from edge import Edge
from neighborhood import Neighborhood


class TestNeighborhood(unittest.TestCase):


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

    def test_neighborhood(self):
        n_a = Neighborhood.get(self.a, self.edges)
        n_b = Neighborhood.get(self.b, self.edges)
        n_c = Neighborhood.get(self.c, self.edges)
        n_d = Neighborhood.get(self.d, self.edges)
        self.assertTrue({self.e1, self.e2} == n_a)
        self.assertTrue({self.e3, self.e4}.isdisjoint(n_a))
        self.assertTrue({self.e1, self.e4} == n_b)
        self.assertTrue({self.e2, self.e3}.isdisjoint(n_b))
        self.assertTrue({self.e3} == n_c)
        self.assertTrue({self.e1, self.e2, self.e4}.isdisjoint(n_c))
        self.assertTrue({self.e2, self.e3, self.e4} == n_d)
        self.assertTrue({self.e1}.isdisjoint(n_d))




if __name__ == '__main__':
    unittest.main(verbosity=2)

