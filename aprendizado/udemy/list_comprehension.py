"""
Usando a LIST COMPREHENSION para encontrar padrões em uma lista e repetí-los em uma nova lista
"""

string = '012345678901234567890123456789012345678901234567890123456789'

n = 10  # variável com a quantidade de caracteres diferentes em cada 'padrão'

contadores = [i for i in range(0, len(string), n)]
tuplas = [(i, i+n) for i in range(0, len(string), n)]
lista = [string[i:i+n] for i in range(0, len(string), n)]
# acima temos a seguinte compreensão: a nova lista recebe o fatiamento da variável string no intervalo de 0 até 10(n)
# do primeiro até o último loop, haverá um salto de mais 10 até chegar ao final da variável string.

raw = [f'string[{i}:{i + n}]' for i in range(0, len(string), n)]
retorno = '.'.join(lista)

print(contadores)
print(tuplas)
print(raw)
print(lista)
print(retorno)
