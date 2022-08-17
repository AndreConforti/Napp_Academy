# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos

import random

idade = []
altura = []
cont = 0

for i in range(30):
    idade.append(random.randint(8, 17))
    altura.append(random.uniform(1.5, 2.0))

media = (sum(altura) / len(altura))

for id in idade:
    if idade[id] > 13:
        if altura[id] < media:
            cont += 1
            print(idade[id])
            print(altura[id])

print(idade)
print(altura)
print(media)
print(cont)