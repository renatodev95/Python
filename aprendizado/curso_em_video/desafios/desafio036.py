# Escreva um programa para aprovar o empréstimo bancário de uma casa. O programa vai perguntar o VALOR DA CASA, o
# SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

valorCasa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
qAnos = int(input('Quantos anos de financiamento? '))
pMensal = valorCasa / (qAnos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f} mensais.'.format(valorCasa, qAnos, pMensal))
if pMensal <= (salario * 0.30):
    print('Empréstimo APROVADO!')
else:
    print('Empréstimo NEGADO!')
