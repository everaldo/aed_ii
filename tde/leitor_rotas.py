# Everaldo Gomes - everaldo.gomes@pucpr.br
# 06/11/2015
#
#
#

from leitor_csv import LeitorCSV
from rota import Rota


ARQUIVO_ROTAS = './data/rotas.csv'
colunas = ('line', 'name')
chave_ordenacao = 'id'

def le_rotas():
    rotas = LeitorCSV.converte(ARQUIVO_ROTAS, colunas)
    return [Rota(r['line'], r['name']) for r in rotas]

