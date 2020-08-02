def calc(cpf):
    cpf_num = cpf
    soma_digi1 = 0
    for chave, multiplicador in enumerate(range(len(cpf_num)+1, 1, -1)):
        print(f'multiplicador: {multiplicador}')
        print(f'chave: {chave}')
        soma_digi1 += int(cpf_num[chave])*multiplicador
    print(soma_digi1)

    