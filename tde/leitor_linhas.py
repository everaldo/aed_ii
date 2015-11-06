# Everaldo Gomes - everaldo.gomes@pucpr.br
# 06/11/2015
#
#
#

from leitor_csv import LeitorCSV
from linha import Linha
from leitor_estacoes import le_estacoes
from leitor_rotas import le_rotas

ARQUIVO_LINHAS = './data/linhas.csv'
colunas = ('station1', 'station2', 'line')


estacoes = le_estacoes()
rotas = le_rotas()

def estacao_por_id(id):
    return next((estacao for estacao in estacoes if int(estacao.id) == int(id)), 'Erro')
def rota_por_id(id):
    return next((rota for rota in rotas if int(rota.id) == int(id)), 'Erro')


def le_linhas():
    linhas = []
    linhas_dict = LeitorCSV.converte(ARQUIVO_LINHAS, colunas)
    for linha in linhas_dict:
        e1 = estacao_por_id(linha['station1'])
        e2 = estacao_por_id(linha['station2'])
        rota = rota_por_id(linha['line'])
        linhas.append(Linha(e1, e2, rota))
    return linhas

