generator = (i**2 for i in range(10) if i % 2 == 0)  # GERA VALOR SOB DEMANDA
for numero in generator:
    print(numero)
