#Desafio 04: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint

pc = randint(1, 3)

escolha = int(input('''
Escolha um número de acordo com as opções:

[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura

Sua escolha: '''))

if pc == 1:
    computador = 'Pedra'
elif pc == 2:
    computador = 'Papel'
else:
    computador = 'Tesoura'

if escolha <= 0 or escolha > 3:
    print('\nOpção inválida!!!')
else:
    if escolha == 1:
        jogador = 'Pedra'
    elif escolha == 2:
        jogador = 'Papel'
    elif escolha == 3:
        jogador = 'Tesoura'

    print(f'\nVocê \033[1;34m{jogador}\033[m X \033[1;31m{computador} \033[mComputador\n\033[0;32m')

    if jogador == 'Pedra':
        if computador == 'Pedra':
            print('JOGO EMPATADO')    
        elif computador == 'Papel':
            print('COMPUTADOR GANHOU')
        else:
            print('VOCÊ GANHOU')
    elif jogador == 'Papel':
        if computador == 'Pedra':
            print('VOCÊ GANHOU')    
        elif computador == 'Papel':
            print('JOGO EMPATADO')
        else:
            print('COMPUTADOR GANHOU')
    else:
        if computador == 'Pedra':
            print('COMPUTADOR GANHOU')    
        elif computador == 'Papel':
            print('VOCÊ GANHOU')    
        else:
            print('JOGO EMPATADO')
    print('\n\033[m')





