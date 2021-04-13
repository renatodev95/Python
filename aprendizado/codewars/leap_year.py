# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

# Crie uma função que determine se o ano (passado como argumento) é bissexto. Se for um ano bissexto retorne True, caso contrário retorne False.

def is_leap(year):
    leap = False
    ano_str = str(year)
    if year % 4 == 0:
        if ano_str[-2:] == '00':
            if year % 400 == 0:
                leap = True
            else:
                return leap
        else:
            leap = True
    return leap


# Se o ano for divisível por 4 será feita outra verificação (se o mesmo termina em '00'), caso termine em um duplo zero será verificado se o resto da divisão por 400 é exata, retornando True caso a verificação seja verdadeira, caso contrário retorna False. Se o ano não terminar em '00' a variavel leap recebe True, pois o ano é divisível por 4.