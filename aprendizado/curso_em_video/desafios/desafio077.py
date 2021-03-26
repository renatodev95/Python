palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador',
            'futuro')
for cont in palavras:  # repetição para verificar as palavras na tupla
    print(f'\nNa palavra {cont.upper()} temos ', end='')
    for letra in cont:  # repetição para verificar as vogais de cada palavra
        # verificada na repetição anterior
        if letra.lower() in 'aáãâeéêiíoóõôuú':
            print(letra, end=' ')
"""Nesse exercício temos que lembrar que cada STRING É UMA LISTA dentro de uma
tupla. Então foi feito outro FOR para mostrar as vogais dentro de cada palavra,
como mostrado acima."""
