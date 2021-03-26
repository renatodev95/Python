# Loop infinito
def valida_cpf(cpf):
    novo_cpf = cpf[:-2]     # Elimina os dois últimos digitos do CPF
    reverso = 10        # Contador reverso
    total = 0
    for index in range(19):
        if index > 8:
            index -= 9

        total += int(novo_cpf[index]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11
            digito = 11 - (total % 11)

            if digito > 9:      # Se digito > 9 seu valor será 0
                digito = 0
            total = 0           # Zera o total
            novo_cpf += str(digito)        # Concatena o digito gerado no novo cpf

    # Evitando sequencias. Ex.: 11111111111, 00000000000...
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    # Checagem para evitar validação de sequencias no CPF
    if cpf == novo_cpf and not sequencia:
        print('CPF válido.')
    else:
        print('CPF inválido.')


cpf_usuario = input('Informe seu CPF: ')

valida_cpf(cpf_usuario)