# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the
# string should be retained.

# Crie uma função que receba uma string como parâmetro e reverta cada palavra contida na string. Todos os espaços da
# instring devem ser mantidos.

def reverse_words(text):
    text = text.split(' ')  # 1º
    new_text = []   # 2º
    for word in text:
        new_text.append(word[::-1])  # 3º
    return ' '.join(new_text)   # 4º


# 1º: Separando o texto com o método split e passando o parâmetro de espaço entre as palavras para separação.

# 2º: Criada uma nova lista que vai receber os caracteres invertidos.

# 3º: Para cada palavra no texto, a nova lista recebe a palavra invertida.

# 4º: A função retorna a junção de todas as strings invertidas.


def reverso(string):
    return ' '.join([s[::-1] for s in string.split(' ')])

# (Esta função reverso é uma refatoração utilizando o método de list comprehension)