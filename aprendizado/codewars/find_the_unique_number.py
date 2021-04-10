# There is an array with some numbers. All numbers are equal except for one. Try to find it!


def find_uniq(arr):
    arr.sort()
    if arr[0] == arr[1]:
        return arr[-1]
    else:
        return arr[0]


lista = [ 1, 1, 1, 2, 1, 1 ]    # exemplo

print(find_uniq(lista))


# Primeiramente é feita a organização da lista em ordem crescente. Se o primeiro valor da lista organizada for igual ao segundo valor, o programa deve retornar o último valor da lista. Caso contrário, deve ser retornado o primeiro valor da lista. Em ambos os casos será retornado o valor único.