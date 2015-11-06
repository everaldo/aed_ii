# Everaldo Gomes - everaldo.gomes@pucpr.br
# 06/11/2015
#
#
#

from leitor_csv import LeitorCSV
from estacao import Estacao


ARQUIVO_ESTACOES = './data/estacoes.csv'
colunas = ('id', 'name')

def le_estacoes():
    estacoes = LeitorCSV.converte(ARQUIVO_ESTACOES, colunas)
    return [Estacao(e['id'], e['name']) for e in estacoes]

