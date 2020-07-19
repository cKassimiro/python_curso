# GERA VALOR SOB DEMANDA
dicionario = {i: i*2 for i in range(50) if i % 2 == 0}
for numero, dobro in dicionario.items():
    print(f'{numero} x 2 = {dobro}')
