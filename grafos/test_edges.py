#
# Everaldo Gomes - everaldo.gomes@pucpr.br
# 29/10/2015
#
#

 
import unittest
from vertex import Vertex
from edge import Edge
from edges import Edges

class TestEdges(unittest.TestCase):


    def setUp(self):
        self.v1 = Vertex()
        self.v2 = Vertex()
        self.v3 = Vertex()
        self.v4 = Vertex()
        self.v5 = Vertex()
        self.e1 = Edge(self.v1, self.v2)
        self.e2 = Edge(self.v2, self.v3)
        self.e3 = Edge(self.v3, self.v4)
        self.e4 = Edge(self.v4, self.v5)
        self.e5 = Edge(self.v1, self.v3)
        self.e6 = Edge(self.v1, self.v4)
        self.e7 = Edge(self.v1, self.v5)
        self.edges = Edges({self.e1, self.e2, \
              self.e3, self.e4, self.e5, \
              self.e6, self.e7})


    def test_size(self):
        """O tamanho de um conjunto de arestas é o número de arestas"""
        self.assertEqual(self.edges.size(), 7)
        e = Edges()
        self.assertEqual(e.size(), 0)
 
    def test_valid_vertice(self):
        """Um vértice é válido se pertence à alguma aresta de E"""
        v = Vertex('v')
        self.assertTrue(self.edges.valid_vertice(self.v1))
        self.assertFalse(self.edges.valid_vertice(v))

    def test_eq(self):
        """Dois conjuntos de arestas são iguais, não importa a ordem"""
        es2 = Edges({self.e7, \
              self.e6, self.e5, self.e4, \
              self.e3, self.e2, self.e1})
        self.assertTrue(self.edges == es2)

    def test_eq_false(self):
        """Dois conjuntos de arestas não são iguais, se não possuem mesmos componentes"""
        es2 = Edges({self.e7, \
              self.e6, self.e5, self.e4, \
              self.e3, self.e2, self.e1, Edge(Vertex(), Vertex())})
        self.assertFalse(self.edges == es2)

    def test_contains(self):
        """É possível utilizar o operador in e not in para verificar pertencimento"""
        self.assertTrue(self.e1 in self.edges)
        self.assertTrue(self.e2 in self.edges)
        self.assertTrue(Edge(Vertex(), Vertex()) not in self.edges)
    
    def test_subset(self):
        """É possível utilizar o operador <= para verificar se é subconjunto"""
        es1 = Edges({self.e1})
        es2 = Edges({self.e2})
        es3 = Edges({self.e1, self.e2, Vertex()})
        eigual = Edges({self.e7, \
              self.e6, self.e5, self.e4, \
              self.e3, self.e2, self.e1})

        self.assertTrue(es1 <= self.edges)
        self.assertTrue(es2 <= self.edges)
        self.assertTrue(eigual <= self.edges)
        self.assertFalse(es3 <= self.edges)
 

    def test_iterator(self):
        """É possível iterar sobre o conjunto de arestas"""
        i = 0
        es = set()
        for e in self.edges:
            es.add(e)
        self.assertEqual(Edges(es), self.edges)

if __name__ == '__main__':
    unittest.main(verbosity=2)
