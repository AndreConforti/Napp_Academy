#Desafio 04: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint

pc = randint(1, 3)

escolha = int(input('''
Escolha um número de acordo com as opções:

[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura

Sua escolha: '''))

if escolha <= 0 or escolha > 3:
    print('\nOpção inválida!!!')
else:
    if escolha == 1:
        if pc == 1:
            print(f'\nVocê \033[1;34m"Pedra"\033[m X \033[1;31m"Pedra" \033[mComputador\n\033[0;32m')
            print('JOGO EMPATADO')    
        elif pc == 2:
            print(f'\nVocê \033[1;34m"Pedra"\033[m X \033[1;31m"Papel" \033[mComputador\n\033[0;32m')
            print('COMPUTADOR GANHOU')
        else:
            print(f'\nVocê \033[1;34m"Pedra"\033[m X \033[1;31m"Tesoura" \033[mComputador\n\033[0;32m')
            print('VOCÊ GANHOU')
    elif escolha == 2:
        if pc == 1:
            print(f'\nVocê \033[1;34m"Papel"\033[m X \033[1;31m"Pedra" \033[mComputador\n\033[0;32m')
            print('VOCÊ GANHOU')    
        elif pc == 2:
            print(f'\nVocê \033[1;34m"Papel"\033[m X \033[1;31m"Papel" \033[mComputador\n\033[0;32m')
            print('JOGO EMPATADO')
        else:
            print(f'\nVocê \033[1;34m"Papel"\033[m X \033[1;31m"Tesoura" \033[mComputador\n\033[0;32m')
            print('COMPUTADOR GANHOU')
    else:
        if pc == 1:
            print(f'\nVocê \033[1;34m"Tesoura"\033[m X \033[1;31m"Pedra" \033[mComputador\n\033[0;32m')
            print('COMPUTADOR GANHOU')    
        elif pc == 2:
            print(f'\nVocê \033[1;34m"Tesoura"\033[m X \033[1;31m"Papel" \033[mComputador\n\033[0;32m')
            print('VOCÊ GANHOU')    
        else:
            print(f'\nVocê \033[1;34m"Tesoura"\033[m X \033[1;31m"Tesoura" \033[mComputador\n\033[0;32m')
            print('JOGO EMPATADO')
    print('\n\033[m')
