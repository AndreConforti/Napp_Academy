import pickle 
import csv
         
def extrair_chaves_dicionario(cidades):
    return list(cidades.keys())

def extrair_tupla_cidades(cidades, estado):
    lista = []
    for cidade in cidades:
        cidade = str(cidade).split(':')
        tupla = (cidade[0], cidade[1], estado)
        lista.append(tupla)
    return lista

def extrair_dados_escolares_por_municipio(dados, id):
    try:
        lista = []
        for registros in dados[id]:
            lista.append(registros)
    except:
       dict = {}
       return dict
    
    return lista

def extrair_dados_municipio__codigo_nome(dados):
    lista = []
    sublista = []
    try:
        for dado in dados:
            lista.append(dado)
        for cidades in lista[1]:
            tupla = (cidades['cod'], cidades['nome'])
            sublista.append(tupla)
        return sublista
    except:
        sublista = []
        return sublista

def extrair_dados_municipio__codigo_nome_situacaoFuncionamento(dados):
    lista = []
    sublista = []
    try:
        for dado in dados:
            lista.append(dado)
        for cidades in lista[1]:
            tupla = (cidades['cod'], cidades['nome'], cidades['situacaoFuncionamentoTxt,'])
            sublista.append(tupla)
        return sublista
    except:
        sublista = []
        return sublista

def extrair_dados_municipio__codigo_nome_situacaoFuncionamento_dependenciaAdministrativa(dados):
        lista = []
        sublista = []
        for dado in dados:
            lista.append(dado)
        for cidades in lista[1]:
            tupla = (cidades['cod'], cidades['nome'], cidades['situacaoFuncionamentoTxt'], cidades['dependenciaAdministrativaTxt'])
            sublista.append(tupla)
        return sublista

def extrair_tupla_dados_municipio(dados, *campos):
        lista = []
        sublista = []
        for dado in dados:
            lista.append(dado)
        for cidades in lista[1]:
            for campo in campos:
                a = tuple((cidades[campo]))
                print(a)
        #     sublista.append(tuple(ovos))
        # return sublista



def gravar_dados_em_CSV(nome_arquivo, campos, dados):
    with open(nome_arquivo, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(campos)
        for dado in dados:
            writer.writerow(dado)
        
if __name__ == "__main__":
    with open('cidades.bin', 'rb') as file:
        cidades = pickle.load(file)
    with open('dados_escolares_id.bin', 'rb') as file:
        dados_escolares_id = pickle.load(file)
    with open('dados_escolares_nome.bin', 'rb') as file:
        dados_escolares_nome = pickle.load(file)
    araras = extrair_dados_escolares_por_municipio(dados_escolares_nome, 'ARARAS')
    dados = extrair_tupla_dados_municipio(araras, 'cod', 'nome', 'dependenciaAdministrativa', 'cidade')
    print(dados)


'''
    # FASE 1: Obter uma lista com ID, cidade e estado.
    estados = extrair_chaves_dicionario(cidades)
    lista_cidades = []
    for estado in estados:
        lista_cidades += extrair_tupla_cidades(cidades[estado], estado)

    # FASE 2: Extrair dados escolares.
    chaves_id = extrair_chaves_dicionario(dados_escolares_id)
    chaves_nome = extrair_chaves_dicionario(dados_escolares_nome)
    
    # Exercício 3
    rio_claro = extrair_dados_escolares_por_municipio(dados_escolares_id, '3543907')
    moji_mirim = extrair_dados_escolares_por_municipio(dados_escolares_nome, 'MOJI MIRIM')
    leme = extrair_dados_escolares_por_municipio(dados_escolares_id, '3526704')
    araras = extrair_dados_escolares_por_municipio(dados_escolares_nome, 'ARARAS')
    
    # Exercício 4
    extrair_dados_municipio__codigo_nome(araras)
    
    # Exercício 5
    extrair_dados_municipio__codigo_nome_situacaoFuncionamento(araras)
    
    # Exercício 6
    extrair_dados_municipio__codigo_nome_situacaoFuncionamento_dependenciaAdministrativa(araras)
    
    # Exercício 7
    mogi_1 = extrair_tupla_dados_municipio(moji_mirim, 'nome', 'cidade') 
    mogi_2 = extrair_tupla_dados_municipio(moji_mirim, 'nome', 'bla', 'cidade') 
    # mogi_1 e mogi_2 terão os mesmos valores.
    campos = ('nome', 'cidade', 'estado', 'situacaoFuncionamentoTxt', 'dependenciaAdministrativaTxt')
    dados_mogi = extrair_tupla_dados_municipio(moji_mirim, *campos) 
    dados_leme = extrair_tupla_dados_municipio(leme, *campos) 

    # Exercício 8
    gravar_dados_em_CSV('mogi_mirim.csv', campos, dados_mogi)
    gravar_dados_em_CSV('leme.csv', campos, dados_leme)
'''