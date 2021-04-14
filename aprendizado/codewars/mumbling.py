# This time no story, no theory. The examples below show you how to write function accum:
# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

# Crie uma função que produza os mesmos resultados dos exemplos acima.

def accum(s):
    list_s = [x for x in s]
    new_list = [(x+1)*y for x, y in enumerate(list_s)]
    return '-'.join([x.capitalize() for x in new_list])
