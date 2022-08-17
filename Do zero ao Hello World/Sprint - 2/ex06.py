# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0

notas = []
mediaGeral = []
cont = 0

for i in range(10):
    print(f'\nAluno {i+1}')
    notas.clear()
    media = 0
    for j in range(4):
        notas.append(float(input(f'{j + 1}ª nota: ')))
    media = sum(notas) / 4
    print(media)
    mediaGeral.append(media)
    if media >= 7:
        cont += 1

print(f'As médias são: {mediaGeral} e o total de média maior ou igual a 7 é {cont}')


