# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

from audioop import reverse

idade = []
altura = []

for i in range(5):
    idade.append(int(input(f'\nIdade da {i+1}ª pessoa: ')))
    altura.append(float(input(f'Altura da {i + 1}ª pessoa: ')))

idade.reverse()
altura.reverse()

print(idade, altura)