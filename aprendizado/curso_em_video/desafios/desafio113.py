# Reescreva a função leiaint() que foi feita no desafio104, incluindo agora a
# possibilidade da digitação de um número de tipo inválido. Aproveite e crie
# uma função leiafloat() coma mesma funcionalidade.

def leiaint(txt):
    while True:
        try:
            n = int(input(txt))
        except (TypeError, ValueError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiafloat(txt):
    while True:
        try:
            n = float(input(txt))
        except (TypeError, ValueError):
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


n1 = leiaint('Digite um Inteiro: ')
n2 = leiafloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}.')
