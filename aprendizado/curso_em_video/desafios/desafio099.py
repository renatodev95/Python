# Faça um programa que tenha uma função chamada maior(), que receba vários
# parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(* num):
    tam = len(num)
    print('Analisando os valores passados...')
    for n in num:
        print(f'{n} ', end='')
    print(f'Foram informados {tam} valores ao todo.')
    for c in range(tam):
        if c == 0:
            maior = num[c]
        else:
            if num[c] > maior:
                maior = num[c]
    print(f'O maior valor informado foi {maior}')


maior(1, 5)
