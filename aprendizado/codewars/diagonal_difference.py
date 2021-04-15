# Crie uma função que retorne o valor absoluto da diferença entre a soma dos valores das diagonais de uma matriz.
# Exemplo:
# 1 2 3
# 4 5 6
# 9 8 9
# A diagonal da esquerda para a direita = 1+5+9 = 15. Da direita para a esquerda diagonal = 3+5+9 = 17. A diferença absoluta deles é |15-17| = 2

# A primeira linha contém um único inteiro, n, o número de linhas e colunas na matriz quadrada arr.
# Cada uma das próximas n linhas descreve uma linha, arr[i], e consiste em  inteiros separados por espaço arr[i][j].

def diagonalDifference(arr):
    d1 = []
    d2 = []
    for x in range(n):
        d1.append(arr[x][x])
        d2.append(arr[x][n-1-x])
    d1 = sum(d1)
    d2 = sum(d2)
    res = abs(d1 - d2)
    return res
