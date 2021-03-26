from datetime import date
sexo = str(input('Qual o seu sexo? [M/F] '))
if sexo == 'F':
    print('Você não precisa se alistar.')
if sexo == 'M':
    nascimento = int(input('Ano de nascimento: '))
    anoatual = date.today().year
    idade = anoatual - nascimento
    print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, anoatual))
    if idade < 18:
        saldo = 18 - idade
        print('Ainda falta {} anos para o alistamento.'.format(saldo))
        print('Seu alistamento será em {}.'.format(anoatual+saldo))
    elif idade > 18:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos.'.format(saldo))
        print('Seu alistamento foi em {}.'.format(anoatual-saldo))
    else:
        print('Você deve se alistar IMEDIATAMENTE.')

if 'F' != sexo != 'M':
    print('SEXO INVALIDO')
