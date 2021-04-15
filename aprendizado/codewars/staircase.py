# Staircase (Escadaria)
# Detalhe da escada
# Esta é uma escada de tamanho n = 4.
#    #
#   ##
#  ###
# ####
# Sua base e altura são iguais a n. Ele é desenhado usando '#' símbolos e espaços.
# A última linha não é precedida de espaços.
# Escreva um programa que imprima uma escada de tamanho n.


def staircase(n):
    space = n - 1
    count = 1
    while count <= n:
        string = ' ' * space
        string += '#' * count
        print(string)
        count = count + 1
        space -= 1


if __name__ == '__main__':
    n = int(input())

    staircase(n)
