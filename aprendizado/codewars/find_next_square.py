# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
# If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.

# Complete o findNextSquaremétodo que encontra o próximo quadrado perfeito integral após aquele passado como parâmetro. Lembre-se de que um quadrado perfeito integral é um inteiro n tal que sqrt (n) também é um inteiro.
# Se o próprio parâmetro não for um quadrado perfeito, -1deve ser retornado. Você pode assumir que o parâmetro não é negativo.

def find_next_square(sq):   # 1
    root = sq**0.5          # 2
    return int((root+1)**2) if float.is_integer(root) else -1   # 3


# 1: A função recebe uma potência (valor positivo);
# 2: A variável raiz recebe a raiz quadrada do valor passado como parâmetro;
# 3: A função retorna o valor inteiro da elevação ao quadrado da 'raiz+1' que
# equivale a potência do número posterior a raiz da potência repassada, se a raiz for um número inteiro (sem ponto flutuante), caso contrário, retorna -1.

