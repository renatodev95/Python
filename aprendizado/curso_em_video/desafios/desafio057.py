# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
if sexo == 'F' or sexo == 'M':
    print('Sexo {} registrado com sucesso!'.format(sexo))
else:
    s = ''
    while sexo != 'M' or sexo != 'F':
        s = str(input('Dados inválidos! Por favor, informe seu sexo: ')).upper().strip()
        if s == 'M' or s == 'F':
            print('Sexo {} registrado com sucesso'.format(s))
            sexo = s
