# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Qual o salário do funcionário? R$'))
aumento = salario + (salario * 0.15)
print('O novo salário do funcionário, com o aumento de 15% é igual a R${:.2f} reais.'.format(aumento))
