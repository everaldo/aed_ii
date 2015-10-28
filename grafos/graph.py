#
# Everaldo Gomes - everaldo.gomes@pucpr.br
# 28/10/2015
#
#

from neighbors import Neighbors

class Graph:


  def __init__(self, vertices = set(), edges = set()):
      self.vertices = vertices
      self.edges = edges

      self.adjacency = {}
      for v in vertices:
          self.adjacency[v] = Neighbors.get(v, edges)


  def __str__(self):
      return(str(self.adjacency))
