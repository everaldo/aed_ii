#
# Everaldo Gomes - everaldo.gomes@pucpr.br
# 28/10/2015
#
#


class Edge:

    cont = 0

    @classmethod
    def get_label(cls):
        label = 'e' + str(cls.cont)
        cls.cont = cls.cont + 1
        return label


    def __init__(self, u, v, label = None):
        if u == v:
            raise Exception("Erro: autoloop não permitido")
        if label is None:
            label = Edge.get_label()
        self.label = "{label}({u}, {v})".format(label=label, u=u, v=v)
        self.e = (u, v)


    def incide(self, v):
        return v in self.e

    # permite usar o operador in e not in para verificar
    # se um vértice incide numa aresta
    def __contains__(self, v):
        return self.incide(v)

    def adjacent(self, v):
        if not v in self.e:
            raise Exception("Erro: {v} não pertence a {e}".format(v=v, e=self.e))
        for u in self.e:
            if u != v:
                return u
                

    def __str__(self):
        return str(self.label)

    __repr__ = __str__

    def __eq__(self, other):
        if type(other) is not Edge:
            return False
        return sorted(self.e) == sorted(other.e)

    def __hash__(self):
        return hash(self.label)


    def __iter__(self):
        self.i = -1
        self.tam = len(self.e)
        return self

    def __next__(self):
        self.i = self.i + 1
        if self.i == self.tam:
            raise StopIteration
        return self.e[self.i]



