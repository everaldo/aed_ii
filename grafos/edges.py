#
# Everaldo Gomes - everaldo.gomes@pucpr.br
# 29/10/2015
#
# A classe Edges representa o conjunto de arestas
#

from itertools import combinations
from edge import Edge

class Edges:

    def __init__(self, edges = set()):
        self.edges = tuple(edges)

    def size(self):
        return len(self.edges)

    def valid_vertice(self, u):
        for e in self.edges:
            if u in e:
                return True
        return False

    def __iter__(self):
        self.i = -1
        self.tam = len(self.edges)
        return self

    def __next__(self):
        self.i = self.i + 1
        if self.i == self.tam:
            raise StopIteration
        return self.edges[self.i]

    def __eq__(self, other):
        return set(self.edges) == set(other.edges)


    def __sub__(self, other):
        es1 = set(self.edges)
        es2 = set(other.edges)
        return Edges(es1 - es2)


    def isdisjoint(self, other):
        return set(self.edges).isdisjoint(set(other.edges))

    @classmethod
    def create(cls, vertices):
        edges_set = set()
        for e in combinations(vertices, 2):
            edges_set.add(Edge(*e))
        return cls(edges_set)


    # Para utilizar o operador <=, representando subconjunto
    def __le__(self, other):
        return set(self.edges) <= set(other.edges)
