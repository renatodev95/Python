print('-'*30, '\nSEQUÊNCIA DE FIBONACCI')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
print('~'*30)
t1, t2 = 0, 1
cont = 1
while cont <= n:
    print(f'{t1} ->', end=' ')
    t1, t2 = t2, t1+t2
    cont += 1
print('Fim')
print('~'*30)
