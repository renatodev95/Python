import time
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
opção = 0
while opção != 5:
    soma = 0
    maior = 0
    multi = 0
    print("""        [1] SOMAR
        [2] MULTIPLICAR
        [3] MAIOR
        [4]NOVOS NÚMEROS
        [5] SAIR DO PROGRAMA""")
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        multi = n1 * n2
        print('A multiplicação entre {} x {} é {}'.format(n1, n2, multi))
    elif opção == 3:
        if n1 != n2 and n1 > n2:
            maior = n1
            print('O maior entre os números digitados foi {}'.format(maior))
            print('=-=' * 10)
        elif n2 != n1 and n2 > n1:
            maior = n2
            print('O maior entre os números digitados foi {}'.format(maior))
        else:
            print('Os números são iguais')
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif opção == 5:
        print('Finalizando...')
        time.sleep(0.5)
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
print('FIM DO PROGRAMA! Volte sempre!')
