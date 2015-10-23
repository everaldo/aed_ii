# Everaldo Gomes - 23/10/2015
# everaldo.gomes@pucpr.br
#
# Demonstra o uso da função itertools.combinations
# para geração de análise combinatória
#
# https://docs.python.org/3/library/itertools.html
#


from itertools import combinations


# A função combinations é ideal para gerar todos os pares
# possíveis de arestas num grafo


# Imprime:

#(1, 2)
#(1, 3)
#(1, 4)
#(2, 3)
#(2, 4)
#(3, 4)

for i in combinations([1, 2, 3, 4], 2):
    print(i)


