tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'quartorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
         'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num < 0 or num > 20:
        while True:
            num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
            if 0 <= num <= 20:
                break
    print(f'Você digitou o número {tupla[num]}')
    resp = str(input('Você deseja continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('Programa finalizado. Volte sempre!')
