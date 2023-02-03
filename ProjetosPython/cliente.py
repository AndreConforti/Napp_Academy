class Cliente():
    def __init__(self, nome, cpf, telefone, endereco):
        self.nome = nome
        self.cpf = cpf.replace('.', '').replace('-','').replace(' ', '').strip()
        self.telefone = telefone.replace('.', '').replace('-','').replace(' ', '').strip()
        self.endereco = endereco

    def veririca_nome(self):
        for letra in self.nome:
            if letra.isdigit():
                return False
            if not letra.isalpha() and not letra.isspace():
                return False
        
        if self.nome == '':
            return False
        
        return True

    def verifica_telefone(self):
        for numero in self.telefone:
            if not numero.isdigit():
                return False
            
        return True

    def verifica_cpf(self):
        for numero in self.cpf:
            if not numero.isdigit():
                return False

        return True

# ====================================================================
if __name__ == '__main__':
    cliente = Cliente('Andre Conforti', '278.759.698-32', '19 988377497', 'Rua José Adami, 485 - Santa Marta - Leme')

    print(cliente.nome)
    teste = cliente.veririca_nome()
    print(teste)
    print(cliente.telefone)
    teste = cliente.verifica_telefone()
    print(teste)
    print(cliente.cpf)
    teste = cliente.verifica_cpf()
    print(teste)