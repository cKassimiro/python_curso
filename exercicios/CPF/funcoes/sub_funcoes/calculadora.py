print(1 * 10)
print(2 * 9)
print(3 * 8)
print(4 * 7)
print(5 * 6)
print(6 * 5)
print(7 * 4)
print(8 * 3)
print(9 * 2)
print(10 * 1)

print(10 + 18 + 24 + 28 + 30 + 30 + 28 + 24 + 18 + 10)

contaCliente = input("Digite seu codigo de verificacao de 3 digitos: ")
verificadorCliente = contaCliente[::-1]
somaNumeroConta = int(contaCliente) + int(verificadorCliente)
multiplicaDigito = list(str(somaNumeroConta))
digitoVerificador = int(
    multiplicaDigito[0]) * 1 + int(multiplicaDigito[1]) * 2 + \
    int(multiplicaDigito[2]) * 3
exibirDigitoVerificador = list(str(digitoVerificador))
print("Valor da verificacao: ",  exibirDigitoVerificador[1])
