#
# Everaldo Gomes - everaldo.gomes@pucpr.br
# 29/10/2015
#
#
#
# https://docs.python.org/3/library/array.html


class IncidenceMatrix:



    def __init__(self, graph):
        self.create_vertices_map(graph.vertices)
        self.matrix = self.create_incidence_matrix(graph)


    def create_vertices_map(self, vertices):
        i = 0
        self.v_map = {}
        self.i_map = {}
        for v in sorted(vertices):
            self.i_map[i] = v
            self.v_map[v] = i
            i = i + 1

    def adjacent(self, u, v):
        return self.matrix[self.v_map[u]][self.v_map[v]]

    def create_incidence_matrix(self, graph):
        matrix = []
        for index, vertice in self.i_map.items():
            matrix.append([])
            for j, u in self.i_map.items():
                if u in graph.adjacency[vertice]:
                    matrix[index].append(1)
                else:
                    matrix[index].append(0)
        return matrix
