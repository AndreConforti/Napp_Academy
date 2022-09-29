# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado
# pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias
# alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser
# encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

try:
    nome = str(input('Nome do atleta: '))
except KeyboardInterrupt:
    print('Não foi informado o nome do atleta. Programa encerrado.')
else: 
    saltos = []
    ficha = []
    for i in range(5):
        saltos.append(float(input(f'{i+1}º salto: ')))

    media = sum(saltos) / len(saltos)

    ficha.append(nome)
    ficha.append(saltos)
    ficha.append(media)

    print(f'''
    Resultado final:
    Atleta: {ficha[0]}
    Saltos: {ficha[1]}
    Média dos saltos: {ficha[2]:.2f}
    ''')