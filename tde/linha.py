# Everaldo Gomes - everaldo.gomes@pucpr.br
# 06/11/2015
#
#
#


class Linha:

    def __init__(self, e1, e2, rota):
        self.e1 = e1
        self.e2 = e2
        self.rota = rota

    def __eq__(self, other):
        if type(other) is not Linha:
            return False
        return self.e1 == other.e1 and self.e2 == other.e2 and \
               self.rota == other.rota

    def __hash__(self):
        return hash(self.e1) + hash(self.e2) + hash(self.rota)

    def __str__(self):
      return "[{rota}: {e1}-{e2}]".format(e1= self.e1, e2=self.e2, rota=self.rota)

    __repr__ = __str__
