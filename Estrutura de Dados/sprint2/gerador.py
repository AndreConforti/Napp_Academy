import pickle 
import requests
import time
import logging
from json.decoder import JSONDecodeError
from sprint2 import extrair_chaves_dicionario
from sprint2 import extrair_tupla_cidades
logging.basicConfig(filename='crawler.log', encoding='utf-8', level=logging.DEBUG)
url = 'http://educacao.dadosabertosbr.com'

def gerar_dump(nome_arquivo, dado):
    with open(nome_arquivo, 'wb') as file_dumped: 
        pickle.dump(dado, file_dumped) 

def carregar_dump(nome_arquivo):
    with open(nome_arquivo, 'rb') as file_dumped:
        dados = pickle.load(file_dumped)    
    return dados

def buscar_lista_cidades_por_estado(estado='sp'):
    path = '/api/cidades/' + str(estado)
    resp = requests.get(url=url+path)
    return resp.json()

def buscar_escolas_em_funcionamento(tupla_cidade):
    id = tupla_cidade[0]
    path = '/api/escolas/buscaavancada?situacaoFuncionamento=1&cidade=' + str(id)
    try:
        resp = requests.get(url=url+path)
        return resp.json()
    except JSONDecodeError:
        logging.error(tupla_cidade)

cidades = {}
estados = ['MG', 'SP', 'RJ', 'ES']
# FASE 1
for estado in estados:
    cidades_encontradas = buscar_lista_cidades_por_estado(estado)
    cidades[estado] = cidades_encontradas

chaves = extrair_chaves_dicionario(cidades)
lista_cidades = []
for estado in chaves:
    lista_cidades += extrair_tupla_cidades(cidades[estado], estado)

# FASE 2

dados_escolares_nome = {}
dados_escolares_id = {}

for cidade in lista_cidades[0:10]:
    logging.debug(cidade)
    dados_coletados = buscar_escolas_em_funcionamento(cidade)
    dados_escolares_nome[cidade[1]] = dados_coletados
    dados_escolares_id[cidade[0]] = dados_coletados
    time.sleep(0.5)


gerar_dump('dados_escolares_id.bin', dados_escolares_id)
gerar_dump('dados_escolares_nome.bin', dados_escolares_nome)

