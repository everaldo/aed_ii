#
# 06/11/2015
#
#

from leitor_csv import LeitorCSV

print(LeitorCSV.converte('data/estacoes.csv', ('id', 'name')))
print(LeitorCSV.converte('data/rotas.csv', ('line', 'name')))
print(LeitorCSV.converte('data/linhas.csv', ('station1', 'station2', 'line')))
