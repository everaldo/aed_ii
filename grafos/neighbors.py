#
# Everaldo Gomes - everaldo.gomes@pucpr.br
# 28/10/2015
#


from neighborhood import Neighborhood

class Neighbors:


    def __init__(self, v, edges):
        self.v = v
        self.edges = edges
        self.compute()
        
        
    def compute(self):
        self.neighbors = set()
        for e in Neighborhood.get(self.v, self.edges):
            self.neighbors.add(e.adjacent(self.v))

    @classmethod
    def get(cls, v, edges):
        instance = cls(v, edges)
        return instance.neighbors
