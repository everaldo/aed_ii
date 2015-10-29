#
# Everaldo Gomes - everaldo.gomes@pucpr.br
# 29/10/2015
#
#

 
import unittest
from vertex import Vertex
from vertices import Vertices
from edge import Edge

class TestVertices(unittest.TestCase):


    def setUp(self):
        self.v1 = Vertex()
        self.v2 = Vertex()
        self.x = Vertex('x')
        self.another_x = Vertex('x')
        self.vertices = Vertices({self.v1, self.v2})


    def test_order(self):
        """A ordem de um conjunto de vértices é seu tamanho"""
        self.assertEqual(self.vertices.order(), 2)
        v = Vertices()
        self.assertEqual(v.order(), 0)
 
    def test_valid_edge(self):
        """Uma aresta é válida se todas suas componentes pertencem a V"""
        e = Edge(self.v1, self.v2)
        e2 = Edge(self.v1, self.x)
        self.assertTrue(self.vertices.valid_edge(e))
        self.assertFalse(self.vertices.valid_edge(e2))

    def test_eq(self):
        """Dois conjuntos de vértices são iguais, não importa a ordem"""
        vs2 = Vertices({self.v2, self.v1})
        self.assertTrue(self.vertices == vs2)

    def test_eq_false(self):
        """Dois conjuntos de vértices não são iguais, se não possuem mesmos componentes"""
        vs2 = Vertices({self.v1, self.v2, Vertex()})
        self.assertFalse(self.vertices == vs2)

    def test_contains(self):
        """É possível utilizar o operador in e not in para verificar pertencimento"""
        self.assertTrue(self.v1 in self.vertices)
        self.assertTrue(self.v2 in self.vertices)
        self.assertTrue(self.x not in self.vertices)
    
    def test_subset(self):
        """É possível utilizar o operador <= para verificar se é subconjunto"""
        vs1 = Vertices({self.v1})
        vs2 = Vertices({self.v2})
        vs3 = Vertices({self.v1, self.v2, Vertex()})
        vigual = Vertices({self.v1, self.v2})
        self.assertTrue(vs1 <= self.vertices)
        self.assertTrue(vs2 <= self.vertices)
        self.assertTrue(vigual <= self.vertices)
        self.assertFalse(vs3 <= self.vertices)
 

    def test_iterator(self):
        """É possível iterar sobre o conjunto de vértices"""
        i = 0
        for v in self.vertices:
            if i == 0:
                self.assertTrue(v == self.v1)
            if i == 1:
                self.assertTrue(v == self.v2)
            i = i + 1



if __name__ == '__main__':
    unittest.main(verbosity=2)
