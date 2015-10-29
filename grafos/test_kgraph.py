#
# Everaldo Gomes - everaldo.gomes@pucpr.br
# 29/10/2015
#
#


import unittest

from vertex import Vertex
from vertices import Vertices
from kgraph import KGraph

class TestKGraph(unittest.TestCase):


    def setUp(self):
        self.a = Vertex('a')
        self.b = Vertex('b')
        self.c = Vertex('c')
        self.d = Vertex('d')
        self.vertices = Vertices({self.a, self.b, self.c, self.d})
        self.kgraph = KGraph.create(self.vertices)


    def test_min_degree(self):
        self.assertEqual(self.kgraph.min_degree(), 3)

    def test_max_degree(self):
        self.assertEqual(self.kgraph.max_degree(), 3)




if __name__ == '__main__':
    unittest.main(verbosity=2)

