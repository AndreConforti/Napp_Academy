# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input('Digite sua altura: '))
genero = str(input('Digite seu gênero "M/F": ')).upper()[0]

if genero == 'M':
  peso = (72.7 * altura) - 58
elif genero == 'F':
  peso = (62.1 * altura) - 44.7
else:
  print('Gênero não especificado')
  peso = 0

print(f'Seu peso ideal é: {peso:.2f}kg')