#
# Everaldo Gomes - everaldo.gomes@pucpr.br
# 28/10/2015
#

from edge import Edge
from edges import Edges

class Neighborhood:
    """A Vizinhança de um vértice v é o conjunto de arestas incidentes em v"""

    def __init__(self, v, edges):
        self.v = v
        self.compute(edges)
        
        
    def compute(self, edges):
        ns = set()
        for e in edges:
            if e.incide(self.v):
                ns.add(e)
        self.neighborhood = Edges(ns)

    @classmethod
    def get(cls, v, edges):
        instance = cls(v, edges)
        return instance.neighborhood
