## Projeto Nós vamos invadir sua praia

Seguir a ------ de Arquiterua Limpa
Como primeira tarefa, devemos identificar as entidades e suas principais funções dentro do programa.

* Cliente
* Quadra
* Agenda
* Aluguel

* Cliente
    - Nome
    - Telefone
    - CPF
    - Endereço (posteriormente pode ser desmembrado para incluir no banco de dados)

* Quadra
    - Número da quadra
    - hora_inicio (início durante a semana)
    - hora_fim (fim durante a semana)
    - Hora_inicio_domingo
    - hora_fim_domingo
    - tempo (1 ou 3 horas)
    - Agenda {data : hora} Dicionário contendo a agenda com as datas e horários
        terca : 09
        terca : 10
        terca : 11
        terca : 12

    - se o tempo for 3 horas pega 
            terca : 9
            terca : 10
            terca : 11
        por exemplo