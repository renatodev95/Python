# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Informe o nome da sua cidade: ')).strip()
divisao = cidade.split()
if divisao[0].upper() == 'SANTO':
    simnao = 'SIM'
else:
    simnao = 'NÃO'

print('O nome da cidade começa com SANTO? {}'.format(simnao))
