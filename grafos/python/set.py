# Everaldo Gomes - 23/10/2015
# everaldo.gomes@pucpr.br
#
# Demonstra o uso da função set
# para geração conjuntos
#
# Conjuntos podem ser utilizados para vértices, arestas
# e em diversos algoritmos de grafos
# https://docs.python.org/3/library/stdtypes.html#set
# https://docs.python.org/3/library/stdtypes.html#frozenset 
#

# Notação Literal - Exceto para conjunto vazio

s = {1}
print(type(s))
# Imprime
#<class 'set'>

s = set()
print(type(s))
# <class 'set'>


# Conjuntos não tem ordem e nem elementos repetidos

s1 = set([1, 2, 3, 4, 1])
s2 = {4, 3, 2, 1}

# Imprime True
print(s1 == s2)



