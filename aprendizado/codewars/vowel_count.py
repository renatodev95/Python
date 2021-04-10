# Contador de Vogais/ Vowel Count

# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

# Retorne o número de vogais em uma string qualquer.
# A entrada da string vai consistir apenas de letras minúsculas e/ou spaços.


def get_count(input_str):
    num_vowels = 0  # 1º
    for letter in input_str.lower():  # 2º
        if letter in 'aeiou':   # 3°
            num_vowels += 1     # 4º
    return num_vowels       # 5º


# 1º: O contador de vogais se inicia zerado

# 2º: Criação de um laço para verificar cada letra ou espaço na string juntamente com a conversão da string total para letras minúsculas.

# 3º: A cada volta do laço é feita a verificação para saber se a letra/espaço está contida em 'aeiou'

# 4º: Se a letra estiver contida em 'aeiou', o contador de vogais é acrescido de mais 1.

# 5º: Retorno com o valor final do contador de vogais.
