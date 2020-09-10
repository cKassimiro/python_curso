# PROFESSOR, TENTEI IMPLEMENTAR O ALGORITMO QUE O SENHOR PROPOS,
# POREM SEM SUCESSO, FIZ O COMUM, QUE É A SEQUENCIA DE DIVIDIR
# POR 2

# FUNÇÃO QUE RECEBE O "DECIMAL" E PROCESSA
# PARA TRANSFORMAR EM "BINARIO" DENTRO DE "CONVERTED"
def convert(value):
    converted = ""
    if value == 0:
        converted = "0" + converted
    else:
        while value > 0:  # ENQUANTO "VALUE" FOR MAIOR QUE 0
            converted = str(value % 2) + converted
            value = value // 2
    return converted
    # RETORNA A LISTA DE STRINGS CONTENDO
    # O VALOR "DECIMAL" EM "BINARIO"


# INSERIR O VALOR QUE DESEJA-SE CONVERTER
decimal = int(input("Insira o valor desejado: \n"))

# PASSA O VALOR "DECIMAL" COMO PARAMETRO
# E EXIBE A SAÍDA DA FUNÇÃO "CONVERT"
print(convert(value=decimal))
