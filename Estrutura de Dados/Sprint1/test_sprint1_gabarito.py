from sprint1 import buscar_sobrenome, buscar_cpf
from sprint1 import buscar_email, buscar_dia_mes_ano
from sprint1 import buscar_dominio, buscar_sub_dominio
from sprint1 import buscar_ip, buscar_dados_navegador
from sprint1 import buscar_endereco, buscar_endereco_estado
from sprint1 import buscar_dados_cartao_credito, buscar_mes_ano_expira_cartao
from sprint1 import listar_nomes, listar_nome_cpf, listar_nome_cpf_ip
import pickle
import pytest

class LoadData:
    def load_list(self):
        with open('lista.bin', 'rb') as list_in_file:
            self.lista = pickle.load(list_in_file)


class Test_buscar_sobrenome(LoadData):
    def test_01(self):
        self.load_list()
        sublista = buscar_sobrenome(self.lista, 'Souza')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 157

    def test_02(self):
        self.load_list()
        sublista = buscar_sobrenome(self.lista)
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 135

    def test_03(self):
        self.load_list()
        sublista = buscar_sobrenome(self.lista, 'Suarez')
        assert isinstance(sublista, list)
        assert len(sublista) == 0


class Test_buscar_cpf(LoadData):
    def test_01(self):
        self.load_list()
        sublista = buscar_cpf(self.lista, '062.748.351-80')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert sublista[0][0] == 'Joaquim Souza'

    def test_02(self):
        self.load_list()
        sublista = buscar_cpf(self.lista, '524.709.861-76')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert sublista[0][0] == 'Luiz Felipe Cardoso'

    def test_03(self):
        self.load_list()
        sublista = buscar_cpf(self.lista, '062.748.351-70')
        assert isinstance(sublista, list)
        assert len(sublista) == 0


class Test_buscar_email(LoadData):
    def test_01(self):
        self.load_list()
        sublista = buscar_email(self.lista, 'ana-beatrizsantos@yahoo.com.br')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 1

    def test_02(self):
        self.load_list()
        sublista = buscar_email(self.lista, 'joao-pedro64@cardoso.org')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 1

    def test_03(self):
        self.load_list()
        sublista = buscar_email(self.lista, 'prof.orlando@nappsolutions.com')
        assert isinstance(sublista, list)
        assert len(sublista) == 0


class Test_buscar_dia_mes_ano(LoadData):
    def test_01(self):
        self.load_list()
        sublista = buscar_dia_mes_ano(self.lista, '20', '03','2022')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 44
        sublista = buscar_dia_mes_ano(self.lista, '19', '03','2022')
        assert len(sublista) == 37
        sublista = buscar_dia_mes_ano(self.lista, '18', '03','2022')
        assert len(sublista) == 31


    def test_02(self):
        self.load_list()
        sublista = buscar_dia_mes_ano(self.lista, dia='20')
        assert isinstance(sublista, list)
        assert len(sublista) == 44
        sublista = buscar_dia_mes_ano(self.lista, mes='02')
        assert len(sublista) == 46

    def test_03(self):
        self.load_list()
        sublista = buscar_dia_mes_ano(self.lista, mes='02', ano='2022')
        assert len(sublista) == 46
        sublista = buscar_dia_mes_ano(self.lista, mes='02', ano='2021')
        assert len(sublista) == 0


class Test_buscar_dominio(LoadData):
    def test_01(self):
        self.load_list()
        sublista = buscar_dominio(self.lista, 'db-13.vieira.br')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 1
        sublista = buscar_dominio(self.lista, 'vieira.br')
        assert len(sublista) == 0

    def test_02(self):
        self.load_list()
        sublista = buscar_dominio(self.lista, 'desktop-75.da.br')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 7
        sublista = buscar_dominio(self.lista, 'da.br')
        assert len(sublista) == 0

    def test_03(self):
        self.load_list()
        sublista = buscar_dominio(self.lista, 'laptop-29.rocha.org')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 1
        sublista = buscar_dominio(self.lista, 'rocha.org')
        assert len(sublista) == 0


class Test_buscar_sub_dominio(LoadData):
    def test_01(self):
        self.load_list()
        sublista = buscar_sub_dominio(self.lista, 'db-13.vieira.br')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 1
        sublista = buscar_sub_dominio(self.lista, 'vieira.br')
        assert len(sublista) == 263

    def test_02(self):
        self.load_list()
        sublista = buscar_sub_dominio(self.lista, 'desktop-75.da.br')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 7
        sublista = buscar_sub_dominio(self.lista, 'da.br')
        assert len(sublista) == 3200

    def test_03(self):
        self.load_list()
        sublista = buscar_sub_dominio(self.lista, 'laptop-29.rocha.org')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 1
        sublista = buscar_sub_dominio(self.lista, 'rocha.org')
        assert len(sublista) == 83


class Test_buscar_ip(LoadData):
    def test_01(self):
        self.load_list()
        sublista = buscar_ip(self.lista, '77.59.227.104')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 1

    def test_02(self):
        self.load_list()
        sublista = buscar_ip(self.lista, '22.96.237.33')
        assert isinstance(sublista, list)
        assert len(sublista) == 1

    def test_03(self):
        self.load_list()
        sublista = buscar_ip(self.lista, '192.168.0.1')
        assert len(sublista) == 0


class Test_buscar_dados_navegador(LoadData):
    def test_01(self):
        self.load_list()
        sublista = buscar_dados_navegador(self.lista, 'Windows NT 6.0')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 163

    def test_02(self):
        self.load_list()
        sublista = buscar_dados_navegador(self.lista, 'Chrome/25.0.897.0')
        assert len(sublista) == 4
        sublista = buscar_dados_navegador(self.lista, 'Chrome/22.0.884.0')
        assert len(sublista) == 3

    def test_03(self):
        self.load_list()
        sublista = buscar_dados_navegador(self.lista, 'Windows XP')
        assert isinstance(sublista, list)
        assert len(sublista) == 0


class Test_buscar_endereco(LoadData):
    def test_01(self):
        self.load_list()
        sublista = buscar_endereco(self.lista, 'Campos / GO')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 1

    def test_02(self):
        self.load_list()
        sublista = buscar_endereco(self.lista, 'Vila São Francisco')
        assert len(sublista) == 18
        sublista = buscar_endereco(self.lista, '87391507')
        assert len(sublista) == 1

    def test_03(self):
        self.load_list()
        sublista = buscar_endereco(self.lista, 'Azevedo / RJ')
        assert len(sublista) == 4
        sublista = buscar_endereco(self.lista, 'Jardim Alvorada')
        assert len(sublista) == 51


class Test_buscar_endereco_estado(LoadData):
    def test_01(self):
        self.load_list()
        sublista = buscar_endereco_estado(self.lista, 'SP')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 371
        sublista = buscar_endereco_estado(self.lista, 'Sp')
        assert len(sublista) == 371
        sublista = buscar_endereco_estado(self.lista, 'sp')
        assert len(sublista) == 371

    def test_02(self):
        self.load_list()
        sublista = buscar_endereco_estado(self.lista, 'RJ')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 387

    def test_03(self):
        self.load_list()
        sublista = buscar_endereco_estado(self.lista, 'Rj')
        assert len(sublista) == 387
        sublista = buscar_endereco_estado(self.lista, 'XX')
        assert len(sublista) == 0


class Test_buscar_dados_cartao_credito(LoadData):
    def test_01(self):
        self.load_list()
        sublista = buscar_dados_cartao_credito(self.lista, 'Mastercard')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 826
        sublista = buscar_dados_cartao_credito(self.lista, 'MasterCard')
        assert len(sublista) == 0
        sublista = buscar_dados_cartao_credito(self.lista, 'MasTeRcArd')
        assert len(sublista) == 0

    def test_02(self):
        self.load_list()
        sublista = buscar_dados_cartao_credito(self.lista, '2232842101941202')
        assert len(sublista) == 1
        sublista = buscar_dados_cartao_credito(self.lista, 'Maestro')
        assert len(sublista) == 786
        
    def test_03(self):
        self.load_list()
        sublista = buscar_dados_cartao_credito(self.lista, '4136024773100748682')
        assert len(sublista) == 1
        sublista = buscar_dados_cartao_credito(self.lista, 'American Express')
        assert len(sublista) == 817


class Test_buscar_mes_ano_expira_cartao(LoadData):
    def test_01(self):
        self.load_list()
        sublista = buscar_mes_ano_expira_cartao(self.lista, '08/28')
        assert isinstance(sublista, list)
        assert isinstance(sublista[0], tuple)
        assert len(sublista) == 80

    def test_02(self):
        self.load_list()
        sublista = buscar_mes_ano_expira_cartao(self.lista, '08/23')
        assert len(sublista) == 103

    def test_03(self):
        self.load_list()
        sublista = buscar_mes_ano_expira_cartao(self.lista, '12/25')
        assert len(sublista) == 90


class Test_listar_nomes(LoadData):
    def test_01(self):
        self.load_list()
        nomes = listar_nomes(self.lista)
        assert isinstance(nomes, list)
        assert isinstance(nomes[0], str)
        assert len(nomes) == 7945

    def test_02(self):
        self.load_list()
        nomes = listar_nomes(self.lista)
        nomes = sorted(nomes)
        assert len(nomes) == 7945
        assert nomes[0] == 'AGATHA ARAGÃO'
        assert nomes[1] == 'AGATHA AZEVEDO'

    def test_03(self):
        self.load_list()
        nomes = listar_nomes(self.lista)
        nomes = sorted(nomes)
        assert len(nomes) == 7945
        assert nomes[-1] == 'YURI SILVEIRA'
        assert nomes[-2] == 'YURI SANTOS'


class Test_listar_nome_cpf(LoadData):
    def test_01(self):
        self.load_list()
        nomes = listar_nome_cpf(self.lista)
        assert isinstance(nomes, list)
        assert isinstance(nomes[0], tuple)
        assert isinstance(nomes[0][0], str)
        assert isinstance(nomes[0][1], str)
        assert len(nomes) == 10000
        assert len(nomes[0]) == 2

    def test_02(self):
        self.load_list()
        nomes = listar_nome_cpf(self.lista)
        nomes = sorted(nomes, key=lambda tup: tup[0], reverse=False)
        assert len(nomes) == 10000
        assert len(nomes[0]) == 2
        assert nomes[0][0] == 'AGATHA ARAGÃO'
        assert nomes[0][1] == '561.498.037-75'
        assert nomes[-1][0] == 'YURI SILVEIRA'
        assert nomes[-1][1] == '310.289.657-02'

    def test_03(self):
        self.load_list()
        nomes = listar_nome_cpf(self.lista)
        nomes = sorted(nomes, key=lambda tup: tup[1], reverse=False)
        assert len(nomes) == 10000
        assert len(nomes[0]) == 2
        assert nomes[0][0] == 'SRTA. MIRELLA SILVA'
        assert nomes[0][1] == '012.369.587-21'
        assert nomes[-1][0] == 'NINA RODRIGUES'
        assert nomes[-1][1] == '987.642.153-00'


class Test_listar_nome_cpf_ip(LoadData):
    def test_01(self):
        self.load_list()
        nomes = listar_nome_cpf_ip(self.lista)
        assert isinstance(nomes, list)
        assert isinstance(nomes[0], tuple)
        assert isinstance(nomes[0][0], str)
        assert isinstance(nomes[0][1], str)
        assert len(nomes) == 10000
        assert len(nomes[0]) == 3

    def test_02(self):
        self.load_list()
        nomes = listar_nome_cpf_ip(self.lista)
        nomes = sorted(nomes, key=lambda tup: tup[0], reverse=False)
        assert len(nomes) == 10000
        assert len(nomes[0]) == 3
        assert nomes[0][0] == 'Agatha aragão'
        assert nomes[0][1] == '561.498.037-75'
        assert nomes[0][2] == '182.76.14.187'
        assert nomes[-1][0] == 'Yuri silveira'
        assert nomes[-1][1] == '310.289.657-02'
        assert nomes[-1][2] == '133.203.207.93'

    def test_03(self):
        self.load_list()
        nomes = listar_nome_cpf_ip(self.lista)
        nomes = sorted(nomes, key=lambda tup: tup[1], reverse=False)
        assert len(nomes) == 10000
        assert len(nomes[0]) == 3
        assert nomes[0][0] == 'Srta. mirella silva'
        assert nomes[0][1] == '012.369.587-21'
        assert nomes[0][2] == '192.100.122.93'
        assert nomes[-1][0] == 'Nina rodrigues'
        assert nomes[-1][1] == '987.642.153-00'
        assert nomes[-1][2] == '64.149.133.120'