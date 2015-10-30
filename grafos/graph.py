#
# Everaldo Gomes - everaldo.gomes@pucpr.br
# 28/10/2015
#
#

from neighbors import Neighbors
from adjacency_matrix import AdjacencyMatrix
from vertices import Vertices
from edges import Edges

class Graph:


    def __init__(self, vertices = Vertices(), edges = Edges()):
        self.vertices = vertices
        self.edges = edges

        self.adjacency = {}
        for v in vertices:
            self.adjacency[v] = Neighbors.get(v, edges)


    def adjacency_matrix(self):
        self.i_matrix = AdjacencyMatrix(self)
        return self.i_matrix

    def degree(self, v):
        len(self.adjacency[v])

    def max_degree(self):
        return max([len(self.adjacency[v]) for v in self.adjacency])

    def min_degree(self):
        return min([len(self.adjacency[v]) for v in self.adjacency])


    def complement(self):
        all_edges = Edges.create(self.vertices)
        return Graph(self.vertices, all_edges - self.edges)

    
    #Para utilizar o operador []
    def __getitem__(self, u):
        if type(u) is Vertices:
            return self.vertex_induced_subgraph(u)
        if type(u) is Edges:
            return self.edge_induced_subgraph(u)
        raise Exception('Um subgrafo deve ser induzido por vértices ou arestas')


    def vertex_induced_subgraph(self, u):
        if not u <= self.vertices:
            raise Exception('O conjunto de vertices {u} \
                não é subconjunto de {v}'.format(u=u, v= self.vertices))
        edgeset = set()
        for e in edges:
            if u.valid_edge(e):
                edgeset.add(e)
        return Graph(u, Edges(edgeset))

    def edge_induced_subgraph(self, m):
        if not m <= self.edges:
            raise Exception('O conjunto de arestas {m} \
                não é subconjunto de {e}'.format(m=m, e= self.edges))
        u = set()
        for v in self.vertices:
            if m.valid_vertices(v):
                u.add(v)
        return Graph(Vertices(u), m)

    @staticmethod
    def complete(vertices = Vertices()):
        return KGraph.create(vertices)

    def __str__(self):
        return(str(self.adjacency))


class KGraph:

    @classmethod
    def create(cls, vertices = Vertices()):
        edges = Edges.create(vertices)
        return Graph(vertices, edges)

