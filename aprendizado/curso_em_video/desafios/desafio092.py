# Crie um programa que leia "nome", "ano de nascimento" e "CTPS" e cadastre-os
# (com "idade") em um dicionário, se por acaso a CTPS for diferente de ZERO, o
# dicionário receberá também o "ano de contratação" e o "salário". Calcule e
# acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

trabalhador = {}
trabalhador['nome'] = str(input("Nome: "))
nasc = int(input("Ano de nascimento: "))
trabalhador["idade"] = date.today().year - nasc
trabalhador["CTPS"] = int(input("Código CTPS (0 não tem): "))
if trabalhador["CTPS"] != 0:
    trabalhador["Ano de Contratação"] = int(input("Ano de Contratação: "))
    trabalhador["Salário"] = float(input("Salário: R$"))
    trabalhador["Aposentadoria"] = (trabalhador["Ano de Contratação"]+35)-nasc
print('=-='*15)
for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}')
