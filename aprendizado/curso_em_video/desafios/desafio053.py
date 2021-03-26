frase1 = str(input('Digite uma frase: ')).strip()
frase = frase1.replace(' ', '')
print('O inverso de {} é {}'.format(frase.upper(), frase1.upper()[::-1].replace(' ', '')))
for c in range(0, 1):
    pali = frase.replace(' ', '')
    if pali == frase[::-1]:
        print('A fase {} é um palindromo'.format(frase))
    else:
        print('Esta frase não é um palindromo')
