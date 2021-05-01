# Função que recebe um limite como parâmetro para retornar uma lista com 
# a sequência de fibonacci (onde o valor do termo seguinte corresponde a soma dos dois termos anteriores).

def fibonacci_one(limit):
    seq = []
    t1 = 0
    t2 = 1
    t3 = 1
    for _ in range(limit):
        seq.append(t3)
        t3 = t1 + t2
        t1 = t2
        t2 = t3
    return seq


def fibonacci_two(limit):
    seq = []
    a, b = 1, 0
    for x in range(limit):
        a, b = b, a+b
        seq.append(a)
    return seq


print(fibonacci_one(26))
