# Faça um programa que leia uma frase pelo teclado e mostre: a)Quantas vezes aparece a letra "A";
# b)Em que posição ela aparece a primeira vez; c)Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).lstrip()
print('A letra "A" apareceu {} vezes na sua frase.'.format(frase.upper().count('A')))
print('A letra "A" apareceu pela primeira vez na posição {} da lista'.format(frase.lower().find('a')+1))
print('A letra "A" apareceu pela última vez na posição {} da lista'.format(frase.lower().rfind('a')+1))
