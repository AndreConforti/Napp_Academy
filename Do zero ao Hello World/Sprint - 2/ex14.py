'''Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa
no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
entre 3 e 4 como "Cúmplice" e 
5 como "Assassino". 
aso contrário, ele será classificado como "Inocente"'''

classificacao = []

print("Responda \"S\" para \"SIM\" ou \"N\" para \"NÃO\"\n")
pergunta = str(input("Telefonou para a vítima? ")).upper().strip()[0]
if pergunta == 'S':
    classificacao.append(pergunta)
pergunta = str(input("Esteve no local do crime? ")).upper().strip()[0]
if pergunta == 'S':
    classificacao.append(pergunta)
pergunta = str(input("Mora perto da vítima? ")).upper().strip()[0]
if pergunta == 'S':
    classificacao.append(pergunta)
pergunta = str(input("Devia para a vítima? ")).upper().strip()[0]
if pergunta == 'S':
    classificacao.append(pergunta)
pergunta = str(input("Já trabalhou com a vítima? ")).upper().strip()[0]
if pergunta == 'S':
    classificacao.append(pergunta)

if len(classificacao) == 2:
    reu = "Susteito"
elif len(classificacao) == 3 or len(classificacao) == 4:
    reu = "Cúmplice"
elif len(classificacao) == 5:
    reu = "Assassino"
else:
    reu = "Inocente" 
    
print(classificacao)
print(f'Diante das respostas, o réu foi considerado: {reu}')