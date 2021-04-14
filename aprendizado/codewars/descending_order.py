# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

# Função que recebe um número inteiro (não negativo) como argumento e o retorna com os dígitos em ordem descendente. Essencialmente, organize os dígitos para criar o maior número possível.

# Primeiro código
def descending_order(num):
    new_num = str(num)
    new_num1 = [int(x) for x in new_num]
    new_num1 = sorted(new_num1, reverse=True)
    string = ''
    for x in new_num1:
        string += str(x)
    return int(string)


# Refatoração do primeiro código (utilizando list comprehension)
def descending_order_two(num):
    return int(''.join([x for x in sorted(str(num), reverse=True)]))
#
#
