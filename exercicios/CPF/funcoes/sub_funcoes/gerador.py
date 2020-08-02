def calc(cpf):
    cpf_inv = cpf
    cpf_list = list(str(cpf_inv))
    verif = int(cpf_list[0])*1 + int(cpf_list[1])*2 + int(cpf_list[2])*3\
        + int(cpf_list[3])*4 + int(cpf_list[4])*5 + int(cpf_list[5])*6\
        + int(cpf_list[6])*7 + int(cpf_list[7])*8 + int(cpf_list[8])*9

    print(f'valor: {verif}')

    cpf_num = cpf
    soma_digi1 = 0
    for chave, multiplicador in enumerate(range(len(cpf_num)+1, 1, -1)):
        print(f'multiplicador: {multiplicador}')
        print(f'chave: {chave}')
        soma_digi1 += int(cpf_num[chave])*multiplicador
    print(soma_digi1)
