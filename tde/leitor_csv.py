# Everaldo Gomes - everaldo.gomes@pucpr.br
# 06/11/2015
#
#
#
import csv

class LeitorCSV:

  def __init__(self, nome_arquivo, lista_chaves):
      """nome_arquivo: caminho do arquivo que será lido. Exemplo data/estacoes.csv
         lista_chaves: lista (ou tupla) com as chaves (colunas) que
                        serão utilizadas do arquivo csv
      """
      self.nome_arquivo = nome_arquivo
      self.lista_chaves = lista_chaves

  @classmethod
  def converte(cls, nome_arquivo, lista_chaves):
      instancia = cls(nome_arquivo, lista_chaves)
      return instancia.leitura()

  def leitura(self):
      registros = []
      with open(self.nome_arquivo) as arquivo_csv:
          leitor = csv.DictReader(arquivo_csv)
          for linha in leitor:
              args = {k: linha[k] for k in self.lista_chaves}
              registros.append(args)
      return registros


