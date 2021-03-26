r = 'S'
cont = soma = media = maior = menor = 0
while r == 'S':
    num = int(input('Digite um número: '))
    r = str(input('Deseja coninuar? [S/N] ')).upper().strip()[0]
    soma += num
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / cont
print('Acabou')
print(f'''A média entre os {cont} números informados foi {media:.2f} 
O maior valor digitado foi {maior} 
O menor valor digitado foi {menor}''')
