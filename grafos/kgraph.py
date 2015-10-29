#
# Everaldo Gomes - everaldo.gomes@pucpr.br
# 29/10/2015
#
# A Classe KGraph representa um Grafo completo
#

from graph import *
from vertices import Vertices
from edges import Edges

class KGraph:

    @classmethod
    def create(cls, vertices = Vertices()):
        edges = Edges.create(vertices)
        return Graph(vertices, edges)

