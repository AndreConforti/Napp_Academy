letra = (input('Digite uma letra: ')).upper().strip()[0]

vogais = 'A B C D E'.split()

if letra.isnumeric():
    print('Você digitou um número.')
else:
    if letra in vogais:
        print('Você digitou uma vogal')
    else:
        print('Você digitou uma consoante')

