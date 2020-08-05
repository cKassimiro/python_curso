def calc(cpf):

    # GERANDO PRIMEIRO DIGITO

    cpf_inv = cpf
    cpf_soma = int(cpf_inv)
    soma_mult = list(str(cpf_soma))
    verif_digi1 = int(soma_mult[0])*10\
        + int(soma_mult[1])*9 + int(soma_mult[2])*8\
        + int(soma_mult[3])*7 + int(soma_mult[4])*6 + int(soma_mult[5])*5\
        + int(soma_mult[6])*4 + int(soma_mult[7])*3 + int(soma_mult[8])*2
    rest_div1 = verif_digi1 % 11
    final_digi1 = 11 - rest_div1
    if final_digi1 > 9:
        digi1 = 0
        soma_mult.append(digi1)
    else:
        digi1 = final_digi1
        soma_mult.append(digi1)

    # GERANDO SEGUNDO DIGITO

    verif_digi2 = int(soma_mult[0])*11\
        + int(soma_mult[1])*10 + int(soma_mult[2])*9\
        + int(soma_mult[3])*8 + int(soma_mult[4])*7 + int(soma_mult[5])*6\
        + int(soma_mult[6])*5 + int(soma_mult[7])*4 + int(soma_mult[8])*3\
        + int(soma_mult[9])*2
    rest_div2 = verif_digi2 % 11
    final_digi2 = 11 - rest_div2
    if rest_div2 > 9:
        digi2 = 0
        soma_mult.append(digi2)
    else:
        digi2 = final_digi2
        soma_mult.append(digi2)

    cpf_final = ''.join(map(str, soma_mult))
    cpf_final =\
        f'{cpf_final[:3]}.{cpf_final[3:6]}.{cpf_final[6:9]}-{cpf_final[9:]}'
    # print('\n' + cpf_final)

    return cpf_final
