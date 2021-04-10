# The first century spans from the year 1 up to and including the year 100, The second - from the year 101 up to and including the year 200, etc.
# Given a year, return the century it is in.

# O primeiro século se estende do ano 1 até e incluindo o ano 100, O segundo - do ano 101 até e incluindo o ano 200, etc.
# Dado um ano, retorne o século em que ele se encontra.

def century(year):
    if year <= 0:   # 1°
        return "Erro! Informe um ano válido."
    elif year % 100 == 0:   # 2°
        return year // 100  
    else:
        return year // 100 + 1  # 3°


# 1º: Impedindo que o sistema aceite valores zerados ou negativos (inválidos para um ano.)

# 2º: Se o resto da divisão do ano por 100 for igual a zero, a função deve retornar o resto da divisão inteira do ano por 100.

# 3º: Caso o resto da divisão do ano por 100 seja DIFERENTE de zero, a função deve retornar o resto da divisão inteira do ano por 100, acrescido de +1.