# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# Um isograma é uma palavra que não contém letras repetidas, consecutivas ou não. Implemente uma função que determina se uma string que possui apenas letras é um isograma. Assuma que uma string vazia é um isograma. Ignore letras maíusculas ou minúsculas.


def is_isogram(string):
    if len(string) >= 1:
        string = string.upper()
        lista = []
        for x in string:
            lista.append(string.count(x))
        soma = sum(lista) / len(lista)
        if soma == 1:
            return True
        else:
            return False
    else:
        return True


print(is_isogram('codewars'))
