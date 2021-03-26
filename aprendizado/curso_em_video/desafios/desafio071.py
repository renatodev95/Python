print('=-='*10)
print('{:^30}'.format('BANCO CEV'))
print('=-='*10)
valor = int(input('Informe o valor que deseja sacar: R$'))
total = valor
cedula = 50
cont = 0
while True:
    if total >= cedula:
        total -= cedula
        cont += 1
    else:
        if cont > 0:
            print(f'Serão liberadas {cont} cédulas de {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        cont = 0
        if total == 0:
            break
print('=-='*10)
print('Volte sempre ao BANCO CEV. Tenha um bom dia!')
