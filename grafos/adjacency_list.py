#
# Everaldo Gomes - everaldo.gomes@pucpr.br
# 30/10/2015
#
#
#
# 


from neighbors import Neighbors
from vertices import Vertices
from edges import Edges

class AdjacencyList:



    def __init__(self, graph):
        self.alist = {}
        for v in graph.vertices:
            self.alist[v] = Neighbors.get(v, graph.edges)

    def adjacent(self, u, v):
        try:
            return v in self.alist[u]
        except KeyError:
            return False

    def get_vertices(self):
        vset = set()
        for v in self.alist:
            vset.add(v)
        return Vertices(vset)


    def get_edges(self):
        eset = set()
        for v, edges in self.alist.items():
            for e in edges:
                eset.add(e)
        return Edges(eset)

    def __getitem__(self, v):
        return self.alist[v]
