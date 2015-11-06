# Everaldo Gomes - everaldo.gomes@pucpr.br
# 06/11/2015
#
#
#


class Estacao:

    def __init__(self, id, nome):
        self.id = int(id)
        self.nome = nome

    def __eq__(self, other):
        if type(other) is not Estacao:
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
      return "{nome}({id})".format(id= self.id, nome=self.nome)

    __repr__ = __str__

