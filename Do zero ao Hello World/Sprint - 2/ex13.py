# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
temperaturas = []
mesesAcima = []

mes = 'Janeiro Fevereiro Março Abril Maio Junho Julho Agosto Setembro Outubro Novembro Dezembro'.split()

for m in mes:
    temperaturas.append(float(input(f'Temperatura para o mês de {m}: ')))

media = sum(temperaturas) / len(temperaturas)

for c, v in enumerate(temperaturas):
    if v > media:
        mesesAcima.append(mes[c])

print(f'Os meses com temperatura acima da média {media:.2f} foram: ', end='')
for j, l in enumerate(mesesAcima):
    print(f'{j + 1} - {l},', end=' ')