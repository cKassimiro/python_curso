def calc(cpf):
    cpf_inv = cpf
    cpf_soma = int(cpf_inv)
    soma_mult = list(str(cpf_soma))
    verif = int(soma_mult[0])*10 + int(soma_mult[1])*9 + int(soma_mult[2])*8\
        + int(soma_mult[3])*7 + int(soma_mult[4])*6 + int(soma_mult[5])*5\
        + int(soma_mult[6])*4 + int(soma_mult[7])*3 + int(soma_mult[8])*2
    rest_div = verif % 11
    final = rest_div - 11
    if final > 9:
        digi1 = 0
        print(f'primeiro digito: {digi1}')
    else:
        digi1 = final
        print(f'primeiro digito: {digi1}')

    print('Valor:', verif)
