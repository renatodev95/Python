# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
# sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER
from datetime import date
nascimento = int(input('Ano de nascimento: '))
idade = date.today().year - nascimento
if idade < 10:
    categoria = 'MIRIM'
elif idade < 15:
    categoria = 'INFANTIL'
elif idade < 20:
    categoria = 'JÚNIOR'
elif idade < 26:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'
print('O atleta tem {} anos.'.format(idade))
print('Classificação: {}'.format(categoria))
