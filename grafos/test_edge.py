#
# Everaldo Gomes - everaldo.gomes@pucpr.br
# 28/10/2015
#
#


import unittest

from vertex import Vertex
from edge import Edge


class TestEdge(unittest.TestCase):


    def setUp(self):
        self.v1 = Vertex()
        self.v2 = Vertex()
        self.x = Vertex('x')
        self.another_x = Vertex('x')


    def test_a_edge_cant_have_autoloop(self):
        with self.assertRaises(Exception):
            Edge(self.x, self.another_x)

    def test_two_edges_are_equal_independent_of_vertices_order(self):
        e1 = Edge(Vertex(1), Vertex(2))
        e2 = Edge(Vertex(2), Vertex(1))
        self.assertEqual(e1, e2)


if __name__ == '__main__':
    unittest.main(verbosity=2)

