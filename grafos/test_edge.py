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
        self.v1 = Vertex(1)
        self.v2 = Vertex(2)
        self.x = Vertex('x')
        self.another_x = Vertex('x')
        self.e12 = Edge(self.v1, self.v2)
        self.e21 = Edge(self.v2, self.v1)


    def test_a_edge_cant_have_autoloop(self):
        """Uma aresta não possui autoloop"""
        with self.assertRaises(Exception):
            Edge(self.x, self.another_x)

    def test_two_edges_are_equal_independent_of_vertices_order(self):
        """Duas arestas são iguais, independentemente da ordem dos vértice"""
        self.assertEqual(self.e12, self.e21)


    def test_incide(self):
        """Um Vértice incide numa aresta, se ele é um de seus componentes"""
        self.assertTrue(self.e12.incide(self.v1))
        self.assertTrue(self.e21.incide(self.v1))
        self.assertTrue(self.e12.incide(self.v2))
        self.assertTrue(self.e21.incide(self.v2))
        self.assertFalse(self.e12.incide(self.x))
        self.assertFalse(self.e21.incide(self.x))
        self.assertTrue(self.x not in self.e21)
        self.assertTrue(self.v1 in self.e12)
        self.assertTrue(self.v1 in self.e21)
        self.assertTrue(self.v2 in self.e12)
        self.assertTrue(self.v2 in self.e12)

    def test_adjacent(self):
        """Os vértices que são pontas das arestas são adjacentes"""
        self.assertTrue(self.e12.adjacent(self.v1), self.v2)
        self.assertTrue(self.e12.adjacent(self.v2), self.v1)
        self.assertTrue(self.e21.adjacent(self.v1), self.v2)
        self.assertTrue(self.e21.adjacent(self.v2), self.v1)

    def test_adjacent_error(self):
        """Se um vértice não pertence à aresta, adjacent retorna um erro"""
        with self.assertRaises(Exception):
            self.e12.adjacent(self.x)

    def test_edge_iteration(self):
        """É possível iterar sobre os vértices de uma aresta"""
        i = 0
        for u in self.e12:
            if i == 0:
               self.assertTrue(u == self.v1)
            if i == 1:
               self.assertTrue(u == self.v2)
            i = i + 1


if __name__ == '__main__':
    unittest.main(verbosity=2)

