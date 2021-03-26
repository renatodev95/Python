# Crie um módulo chamado "moeda.py", que tenha as funções incorporadas
# aumentar(), diminuir(), dobro(), e metade().
# Faça também um programa que importe esse módulo e use essas funções.
from exercicio107 import moeda

p = float(input("Digite o preço: \nR$"))
print(f'A metade de R${p} é {moeda.metade(p)}')
print(f'O dobro de R${p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')
