#
# Everaldo Gomes - everaldo.gomes@pucpr.br
# 29/10/2015
#
# A classe Vertices representa um conjunto de vértices
# Ela é conveniente porque permite o mapeamento de
# vértices com índices inteiros
#


class Vertices:

    def __init__(self, vertices = set()):
        self.vertices = tuple(sorted(vertices))

    def order(self):
        return len(self.vertices)

    def __len__(self):
        return self.order()

    def valid_edge(self, edge):
        for v_i in edge:
            if v_i not in self:
                return False
        return True

    def isdisjoint(self, other):
        return set(self.vertices).isdisjoint(set(other.vertices))



    def __iter__(self):
        self.i = -1
        self.tam = len(self.vertices)
        return self

    def __next__(self):
        self.i = self.i + 1
        if self.i == self.tam:
            raise StopIteration
        return self.vertices[self.i]

    def __eq__(self, other):
        return set(self.vertices) == set(other.vertices)

    # Para utilizar o operador in e not in
    def __contains__(self, v):
        return v in self.vertices

    # Para utilizar o operador <=, representando subconjunto
    def __le__(self, other):
        return set(self.vertices) <= set(other.vertices)
