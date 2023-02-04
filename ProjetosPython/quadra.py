import datetime
from datetime import datetime

class Quadra():
    def __init__(self, nome, hora_inicio, hora_fim, duracao, hora_inicio_domingo=None, hora_fim_domingo=None):
        self.nome = nome
        self.agenda = {}
        self.hora_inicio = hora_inicio    # datetime.strptime(hora_inicio, '%H:%M').time()
        self.hora_fim = hora_fim          # datetime.strptime(hora_fim, '%H:%M').time()
        self.hora_inicio_domingo = hora_inicio_domingo
        self.hora_fim_domingo = hora_fim_domingo
        self.duracao_aluguel = duracao

    def verificar_disponibilidade(self, data, hora_inicio, hora_fim, duracao):
        data = datetime.strptime(data, "%Y-%m-%d")
        
        if duracao not in [1, 3]:
            return False

        elif data.weekday() == 0: # Verifica se é segunda-feira
            return False

        elif data.weekday() == 6: # Verifica se é domingo
            if (hora_inicio >= self.hora_inicio_domingo and hora_inicio < self.hora_fim_domingo) and \
               (hora_fim > self.hora_inicio_domingo and hora_fim <= self.hora_fim_domingo):
               return True
            else:
                return False

        else: # Se é um dia válido, verifica se está dentro do horário
            if (hora_inicio >= self.hora_inicio and hora_inicio < self.hora_fim) and \
               (hora_fim > self.hora_inicio and hora_fim <= self.hora_fim):
               return True
            else:
                return False


# =====================================================================================
if __name__ == '__main__':
    quadra = Quadra('Quadra 1', '09:00', '22:00', 1)

    teste = quadra.verificar_disponibilidade('2023-02-04', '10:00', '11:00', 1)

    print(teste)
