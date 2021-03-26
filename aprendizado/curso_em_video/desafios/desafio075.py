a = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')),
     int(input('Digite um número: ')))
print(f'Você digitou os valores {a}')
if 9 in a:
    print(f'O número 9 apareceu {a.count(9)} vezes.')
else:
    print('O número 9 não foi digitado nenhuma vez')
if 3 in a:
    print(f'O número 3 foi digitado na {a.index(3)+1}° posição')
else:
    print('O número 3 não foi digitado nenhuma vez')
print('Os números pares informados foram: ', end='')
for c in range(0, len(a)):
    if a[c] % 2 == 0:
        print(a[c], end=' ')
