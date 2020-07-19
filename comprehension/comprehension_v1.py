# [ expressão for item in list ]
dobros = [i * 2 for i in range(100000)]

# VERSÃO 'NORMAL'
dobro = []
for i in range(20):
    dobro.append(i * 2)
print(dobro)

# GERANDO DOCUMENTO DE SAIDA
with open('dobros.txt', 'w') as saida:
    print(dobros, file=saida)
