#
# Everaldo Gomes - everaldo.gomes@pucpr.br
# 28/10/2015
#


from neighborhood import Neighborhood
from vertices import Vertices

class Neighbors:
    """Os vizinhos de um vértice v são o conjunto de vértices da Vizinhança"""

    def __init__(self, v, edges):
        self.v = v
        self.compute(edges)
        
        
    def compute(self, edges):
        ns = set()
        for e in Neighborhood.get(self.v, edges):
            ns.add(e.adjacent(self.v))
        self.neighbors = Vertices(ns)

    @classmethod
    def get(cls, v, edges):
        instance = cls(v, edges)
        return instance.neighbors
