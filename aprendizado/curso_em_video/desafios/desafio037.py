# Faça um programa que leia um numero inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1
# para binário, 2 para octal e 3 para hexadecimal.
n = int(input('Digite um número inteiro: '))
print("""Escolha uma das bases para conversão:
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL""")
escolha = int(input('Sua opção: '))
if escolha == 1:
    print('O número {} convertido para BINÁRIO é igual a {}.'.format(n, bin(n)[2:]))
elif escolha == 2:
    print('O número {} convertido para OCTAL é igual a {}.'.format(n, oct(n)[2:]))
elif escolha == 3:
    print('O número {} convertido para HEXADECIMAL é igual a {}.'.format(n, hex(n)[2:]))
else:
    print('[ERRO] Digite uma opção válida.')
