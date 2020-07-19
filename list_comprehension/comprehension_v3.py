generator = (i**2 for i in range(10) if i % 2 == 0)  # GERA VALOR SOB DEMANDA
print(next(generator))  # 0
print(next(generator))  # 4
print(next(generator))  # 16
print(next(generator))  # 36
print(next(generator))  # 64
# print(next(generator)) # Erro!
