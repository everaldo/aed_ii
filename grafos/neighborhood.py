#
# Everaldo Gomes - everaldo.gomes@pucpr.br
# 28/10/2015
#

from edge import Edge

class Neighborhood:


    def __init__(self, v, edges):
        self.v = v
        self.edges = edges
        self.compute()
        
        
    def compute(self):
        self.neighborhood = set()
        for e in self.edges:
            if e.incide(self.v):
                self.neighborhood.add(e)

    @classmethod
    def get(cls, v, edges):
        instance = cls(v, edges)
        return instance.neighborhood
