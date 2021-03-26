from datetime import date
ano = date.today().year
menor = 0
maior = 0
for c in range(1, 8):
    nascimento = int(input('Em que ano a {}ª pesoa nasceu? '.format(c)))
    if ano - nascimento < 21:
        menor += 1
    else:
        maior += 1
print("""Resultado:
*Pessoas que ainda não atingiram a maioridade: {}
*Pessoas que já são maiores: {}""".format(menor, maior))
