import requests
from http import HTTPStatus
from json.decoder import JSONDecodeError
from sprint2 import extrair_tupla_cidades
from sprint2 import extrair_tupla_dados_municipio
from sprint2 import gravar_dados_em_CSV
import logging

logging.basicConfig(filename='consumo_API.log', level=logging.DEBUG)
url = 'http://educacao.dadosabertosbr.com'

def buscar_lista_cidades_por_estado(estado='sp'):
    path = '/api/cidades/' + str(estado)
    resp = requests.get(url=url+path)
    if resp.status_code == HTTPStatus.OK:
        return resp.json()
    else:
        logging.debug('Erro ao acessar servidor: ')
        logging.debug('Função: buscar_lista_cidades_por_estado')
        logging.debug(estado)
        return []

def buscar_escolas_em_funcionamento(tupla_cidade):
    id = tupla_cidade[0]
    path = '/api/escolas/buscaavancada?situacaoFuncionamento=1&cidade=' + str(id)
    resp = requests.get(url=url+path)
    if resp.status_code == HTTPStatus.OK:
        return resp.json()
    else:
        logging.debug('Erro ao acessar servidor: ')
        logging.debug('Função: buscar_escolas_em_funcionamento')
        logging.debug(tupla_cidade)
        return []

cidades = {}
estados = ['SC', 'PR', 'RS']
for estado in estados:
    cidades_encontradas = buscar_lista_cidades_por_estado(estado)
    cidades[estado] = cidades_encontradas

lista_cidades = []
for estado in estados:
    lista_cidades += extrair_tupla_cidades(cidades[estado], estado)

campos = ('nome', 'cidade', 'estado', 'situacaoFuncionamentoTxt', 'dependenciaAdministrativaTxt')
for cidade in lista_cidades:
    logging.info(cidade)
    dados_coletados = buscar_escolas_em_funcionamento(cidade)
    try:
        dados_processados = extrair_tupla_dados_municipio(dados_coletados, *campos)
        nome_arquivo = cidade[1].replace(' ','_').lower()
        nome_arquivo = 'planilhas/' + nome_arquivo + '.csv'
        gravar_dados_em_CSV(nome_arquivo, campos, dados_processados)
    except:
        logging.debug('Erro no processamento de: ')
        logging.debug(cidade)
    