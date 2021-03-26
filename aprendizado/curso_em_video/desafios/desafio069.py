msg = 'CADASTRE UMA PESSOA'
totmais18 = 0
tothomens = 0
totmmenos20 = 0
while True:
    print('-'*40)
    print(f'{msg:^40}')
    print('-' * 40)
    while True:
        idade = int(input('Idade: '))
        if idade > 0:
            break
    while True:
        sexo = str(input('Sexo[M/F]: ')).upper().strip()[0]
        if sexo in 'MmFf':
            break
    while True:
        opção = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
        if opção in 'SsNn':
            break
    if idade > 18:
        totmais18 += 1
    if sexo == 'M':
        tothomens += 1
    if sexo == 'F' and idade < 20:
        totmmenos20 += 1
    if opção == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {totmais18}')
print(f'Ao todo temos {tothomens} homens cadastrados.')
print(f'E temos {totmmenos20} mulheres com menos de 20 anos.')
