def calc(cpf):
    cpf_inv = cpf
    cpf_soma = int(cpf_inv)
    soma_mult = list(str(cpf_soma))
    verif = int(soma_mult[0])*10 + int(soma_mult[1])*9 + int(soma_mult[2])*8\
        + int(soma_mult[3])*7 + int(soma_mult[4])*6 + int(soma_mult[5])*5\
        + int(soma_mult[6])*4 + int(soma_mult[7])*3 + int(soma_mult[8])*2
    div = verif * (10/11)
    print(div)
    print('Valor:', verif)

    # cpf_num = cpf
    # soma_digi1 = 0
    # for chave, multiplicador in enumerate(range(len(cpf_num)+1, 1, -1)):
    #     print(f'multiplicador: {multiplicador}')
    #     print(f'chave: {chave}')
    #     soma_digi1 += int(cpf_num[chave])*multiplicador
    # print(soma_digi1)
