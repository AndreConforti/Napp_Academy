import pickle 
from datetime import datetime
from time import strftime
         
def buscar_sobrenome(lista, sobrenome='Silva'):
    sublista = []
    for item in lista:
        if sobrenome in item[0]:
            sublista.append(item)
    return sublista

def buscar_cpf(lista, cpf):
    pass

def buscar_email(lista, email):
    pass

def buscar_dia_mes_ano(lista, dia='22',mes='03',ano='2022'):
    sublista = []
    for registro in lista:
        data = registro[3][:10]
        if data == f'{ano}-{mes}-{dia}':
            print(data)
            sublista.append(registro)
    return (sublista)

def buscar_dominio(lista, dominio):
    pass

def buscar_sub_dominio(lista, dominio):
    pass

def buscar_ip(lista, ip):
    pass

def buscar_dados_navegador(lista, navegador):
    pass

def buscar_endereco(lista, endereco):
    pass

def buscar_endereco_estado(lista, estado):
    pass

def buscar_dados_cartao_credito(lista, cartao):
    pass

def buscar_mes_ano_expira_cartao(lista, cartao_expira):
    pass

def listar_nomes(lista):
    nomes = []
    for item in lista:
        nomes.append(item[0].upper())
    return list(set(nomes))

def listar_nome_cpf(lista):
    pass

def listar_nome_cpf_ip(lista):
    pass

if __name__ == "__main__":
    with open('lista.bin', 'rb') as list_in_file:
        lista = pickle.load(list_in_file)
    buscar_sobrenome(lista)


resp = buscar_dia_mes_ano(lista)
print(resp)
