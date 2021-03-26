media = 0
soma = 0
maior = 0
mulheres = 0
velho = ''
for c in range(1, 5):
    print('-'*5, ' {}ª PESSOA '.format(c), '-'*5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma += idade
    if sexo.upper() == 'M':
        if idade > maior:
            maior = idade
            velho = nome
    if sexo.upper() == 'F':
        if idade < 20:
            mulheres += 1
media = soma / 4
print('A média de idade do grupo é {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maior, velho))
print('A quantidade de mulheres que tem menos de 20 anos é {}'.format(mulheres))
