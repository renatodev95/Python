# Faça um programa que tenha uma função notas() que pode receber várias notas
# de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
def notas(* n, sit=False):
    """
    [funcao notas]
        :param n: uma ou mais notas dos alunos (aceita varias)
        :param sit (bool, optional): Valor opcional, indicando se deve ou nao
        adicionar a situacao.
        :return: retorna um dicionario com varias informacoes sobre a situacao
        da turma.
    """
    note = {}
    note['total'] = len(n)
    note['maior'] = max(n)
    note['menor'] = min(n)
    media = sum(n)/len(n)
    note['média'] = media
    if sit:
        if media < 5:
            note['situação'] = 'RUIM'
        elif 5 < media < 7:
            note['situação'] = 'RAZOÁVEL'
        else:
            note['situação'] = 'BOA'
    return note


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
