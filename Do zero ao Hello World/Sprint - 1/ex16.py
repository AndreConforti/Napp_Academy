# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area = float(input('Informe a área a ser pintada em metros: '))

cobertura_tinta = area / 3
capacidade_lata = 18
valor_lata = 80

quantidade_latas = int(cobertura_tinta // capacidade_lata)

if quantidade_latas == 0:
  quantidade_latas = 1

if cobertura_tinta % quantidade_latas != 0:
  quantidade_latas += 1

total = quantidade_latas * valor_lata

print(f'Quantidade de latas = {quantidade_latas}')
print(f'Valor total a pagar = R$ {total}')
