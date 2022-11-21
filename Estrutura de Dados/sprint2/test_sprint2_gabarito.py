from sprint2 import extrair_chaves_dicionario
from sprint2 import extrair_tupla_cidades
from sprint2 import extrair_dados_escolares_por_municipio
from sprint2 import extrair_dados_municipio__codigo_nome
from sprint2 import extrair_dados_municipio__codigo_nome_situacaoFuncionamento
from sprint2 import extrair_dados_municipio__codigo_nome_situacaoFuncionamento_dependenciaAdministrativa
from sprint2 import extrair_tupla_dados_municipio
import pickle
import pytest

class LoadData:
    def load_list(self):
        with open('cidades.bin', 'rb') as file:
            self.cidades = pickle.load(file)

        with open('dados_escolares_id.bin', 'rb') as file:
            self.dados_escolares_id = pickle.load(file)

        with open('dados_escolares_nome.bin', 'rb') as file:
            self.dados_escolares_nome = pickle.load(file)

class Test_extrair_chaves_dicionario(LoadData):
    def test_01(self):
        self.load_list()
        chaves = extrair_chaves_dicionario(self.cidades)
        assert isinstance(chaves, list)
        assert isinstance(chaves[0], str)
        assert len(chaves) == 4

    def test_02(self):
        chaves = extrair_chaves_dicionario({})
        assert isinstance(chaves, list)
        assert len(chaves) == 0

    def test_03(self):
        msg_erro = "'list' object has no attribute 'keys'"
        with pytest.raises(AttributeError) as error:
            extrair_chaves_dicionario([0,1,2])
        assert str(error.value) == msg_erro

class Test_extrair_tupla_cidades(LoadData):
    def test_01(self):
        cidades = ['3500907:ALTAIR','3501004:ALTINOPOLIS',
                 '3501103:ALTO ALEGRE', '3501152:ALUMINIO',
                 '3501202:ALVARES FLORENCE']
        tuplas = extrair_tupla_cidades(cidades, 'SP')
        assert isinstance(tuplas, list)
        assert isinstance(tuplas[0], tuple)
        assert len(tuplas) == 5
        assert len(tuplas[0]) == 3
        assert tuplas[0][-1] == 'SP'
        assert tuplas[0][0] == '3500907'
        assert tuplas[0][1] == 'ALTAIR'

#FASE 2

class Test_extrair_dados_escolares_por_municipio(LoadData):
    def test_cidade_leme(self):
        self.load_list()
        dados = extrair_dados_escolares_por_municipio(self.dados_escolares_nome, 'LEME')
        assert isinstance(dados, list)
        assert isinstance(dados[0], int)
        assert isinstance(dados[1], list)
        assert len(dados) == 2
        assert len(dados[1]) == 75

    def test_cidade_moji_mirim(self):
        self.load_list()
        dados = extrair_dados_escolares_por_municipio(self.dados_escolares_nome, 'MOJI MIRIM')
        assert isinstance(dados, list)
        assert isinstance(dados[0], int)
        assert isinstance(dados[1], list)
        assert len(dados) == 2
        assert len(dados[1]) == 55

    def test_cidade_vazio(self):
        self.load_list()
        dados = extrair_dados_escolares_por_municipio(self.dados_escolares_nome, 'BRASILIA')
        assert isinstance(dados, dict)
        assert len(dados) == 0
        

class Test_extrair_dados_escolares_por_municipio_2(LoadData):
    def test_cidade_3151404(self):
        self.load_list()
        dados = extrair_dados_escolares_por_municipio(self.dados_escolares_id, '3151404')
        assert isinstance(dados, list)
        assert isinstance(dados[0], int)
        assert isinstance(dados[1], list)
        assert len(dados) == 2
        assert len(dados[1]) == 27

    def test_cidade_3143401(self):
        self.load_list()
        dados = extrair_dados_escolares_por_municipio(self.dados_escolares_id, '3143401')
        assert isinstance(dados, list)
        assert isinstance(dados[0], int)
        assert isinstance(dados[1], list)
        assert len(dados) == 2
        assert len(dados[1]) == 15

    def test_cidade_vazio(self):
        self.load_list()
        dados = extrair_dados_escolares_por_municipio(self.dados_escolares_id, '9999999')
        assert isinstance(dados, dict)
        assert len(dados) == 0

class Test_extrair_dados_municipio__codigo_nome(LoadData):
    def test_extrair_cenario1(self):
        self.load_list()
        araras = extrair_dados_escolares_por_municipio(self.dados_escolares_nome, 'ARARAS')
        dados = extrair_dados_municipio__codigo_nome(araras)
        assert isinstance(dados, list)
        assert len(dados) == 84
        assert isinstance(dados[0], tuple)
        assert len(dados[0]) == 2
        assert isinstance(dados[0][0], int)
        assert isinstance(dados[0][1], str)

    def test_extrair_cenario2(self):
        self.load_list()
        leme = extrair_dados_escolares_por_municipio(self.dados_escolares_nome, 'LEME')
        dados = extrair_dados_municipio__codigo_nome(leme)
        assert isinstance(dados, list)
        assert len(dados) == 75
        assert isinstance(dados[0], tuple)
        assert len(dados[0]) == 2
        assert isinstance(dados[0][0], int)
        assert isinstance(dados[0][1], str)


class Test_extrair_dados_municipio__codigo_nome(LoadData):
    def test_extrair_cenario1(self):
        self.load_list()
        araras = extrair_dados_escolares_por_municipio(self.dados_escolares_nome, 'ARARAS')
        dados = extrair_dados_municipio__codigo_nome_situacaoFuncionamento_dependenciaAdministrativa(araras)
        assert isinstance(dados, list)
        assert len(dados) == 84
        assert isinstance(dados[0], tuple)
        assert len(dados[0]) == 4
        assert isinstance(dados[0][0], int)
        assert isinstance(dados[0][1], str)

    def test_extrair_cenario2(self):
        self.load_list()
        leme = extrair_dados_escolares_por_municipio(self.dados_escolares_nome, 'LEME')
        dados = extrair_dados_municipio__codigo_nome_situacaoFuncionamento_dependenciaAdministrativa(leme)
        assert isinstance(dados, list)
        assert len(dados) == 75
        assert isinstance(dados[0], tuple)
        assert len(dados[0]) == 4
        assert isinstance(dados[0][0], int)
        assert isinstance(dados[0][1], str)
        

class Test_extrair_tupla_dados_municipio(LoadData):
    def test_extrair_cenario1(self):
        self.load_list()
        araras = extrair_dados_escolares_por_municipio(self.dados_escolares_nome, 'ARARAS')
        dados = extrair_tupla_dados_municipio(araras, 'nome', 'cidade')
        assert isinstance(dados, list)
        assert len(dados) == 84
        assert isinstance(dados[0], tuple)
        assert len(dados[0]) == 2
        assert isinstance(dados[0][0], str)
        assert isinstance(dados[0][1], str)

    def test_extrair_cenario2(self):
        self.load_list()
        araras = extrair_dados_escolares_por_municipio(self.dados_escolares_nome, 'ARARAS')
        dados = extrair_tupla_dados_municipio(araras, 'cod', 'nome', 'dependenciaAdministrativa', 'cidade')
        assert isinstance(dados, list)
        assert len(dados) == 84
        assert isinstance(dados[0], tuple)
        assert len(dados[0]) == 4
        assert isinstance(dados[0][0], int)
        assert isinstance(dados[0][1], str)
        assert isinstance(dados[0][2], int)
        assert isinstance(dados[0][3], str)

    def test_extrair_cenario3(self):
        self.load_list()
        araras = extrair_dados_escolares_por_municipio(self.dados_escolares_nome, 'ARARAS')
        dados = extrair_tupla_dados_municipio(araras, 'cod', 'nome')
        assert isinstance(dados, list)
        assert len(dados) == 84
        assert isinstance(dados[0], tuple)
        assert len(dados[0]) == 2
        assert isinstance(dados[0][0], int)
        assert isinstance(dados[0][1], str)

    def test_extrair_cenario4(self):
        self.load_list()
        araras = extrair_dados_escolares_por_municipio(self.dados_escolares_nome, 'ARARAS')
        dados = extrair_tupla_dados_municipio(araras, 'cod', 'bla', 'nome', 'bla')
        assert isinstance(dados, list)
        assert len(dados) == 84
        assert isinstance(dados[0], tuple)
        assert len(dados[0]) == 2
        assert isinstance(dados[0][0], int)
        assert isinstance(dados[0][1], str)

    def test_extrair_cenario5(self):
        self.load_list()
        araras = extrair_dados_escolares_por_municipio(self.dados_escolares_nome, 'ARARAS')
        dados = extrair_tupla_dados_municipio(araras, 'campo_invalido1', 'campo_invalido2','campo_invalido3')
        assert isinstance(dados, list)
        assert len(dados) == 84
        assert isinstance(dados[0], tuple)
        assert len(dados[0]) == 0
