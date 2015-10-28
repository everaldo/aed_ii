#
# Everaldo Gomes - everaldo.gomes@pucpr.br
# 28/10/2015
#
#

class Vertex:

    cont = 0

    @classmethod
    def get_label(cls):
        label = str(cls.cont)
        cls.cont = cls.cont + 1
        return label

    def __init__(self, label = None):
        if label is None:
            label = Vertex.get_label()
        self.label = str(label)


    def __str__(self):
        return str(self.label)

    __repr__ = __str__

    def __eq__(self, other):
        if type(other) is not Vertex:
            return False
        return self.label == other.label

    def __hash__(self):
        return hash(self.label)

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.label < other.label

    def __gt__(self, other):
        return self.label > other.label

    def __le__(self, other):
        return self.label <= other.label

    def __ge__(self, other):
        return self.label >= other.label
