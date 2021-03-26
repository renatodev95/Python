# Crie um módulo chamado "moeda.py", que tenha as funções incorporadas
# aumentar(), diminuir(), dobro(), e metade().
# Faça também um programa que importe esse módulo e use essas funções.

import moeda

p = float(input("Digite o preço: R$"))
moeda.resumo(p, 10, 5)
