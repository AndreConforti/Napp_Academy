# Desafio 03: Desenvolva uma lógica que leia o peso e a altura de
#           uma pessoa, calcule seu Índice de Massa Corporal (IMC)
#           e mostre seu status, de acordo com a tabela abaixo:
#             - IMC abaixo de 18,5: Abaixo do Peso
#             - Entre 18,5 e 25: Peso Ideal
#             - 25 até 30: Sobrepeso
#             - 30 até 40: Obesidade
#             - Acima de 40: Obesidade Mórbida

peso = float(input('Digite seu peso em "kg": '))
alt = float(input('Digite sua altura em "m": '))

imc = peso / (alt * alt)

if   imc < 18.5:
    classificacao = 'Abaixo do Peso'
elif 18.5 <= imc < 25:
    classificacao = 'Peso Ideal'
elif 25 <= imc < 30:
    classificacao = 'Sobrepeso'
elif 30 <= imc < 40: 
    classificacao = 'Obesidade'
else:
    classificacao = 'Obesidade Mórbida'

print(f'De acordo com o peso e altura informados, seu IMC é {imc:.2f} e sua classificação é: {classificacao}')