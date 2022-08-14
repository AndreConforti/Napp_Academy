peso = float(input("Informe o peso de peixes: "))

excesso = peso - 50

multa = excesso * 4

if peso < 50:
  print('Você não excedeu o limite de peso. Portanto, não há multa.')
else:
  print(f'Você ultrapassou o limite em {excesso} kg. Portanto, sua multa será no valor de R$ {multa:.2f}')

