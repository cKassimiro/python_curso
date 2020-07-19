# [ expressão for item in list ]
dobros = [i * 2 for i in range(20)]

# VERSÃO 'NORMAL'
somas = []
for i in range(20):
    somas.append(i + 1)
    print(somas)


# GERANDO DOCUMENTO DE SAIDA
with open('dobros.txt', 'w') as saida:
    print(dobros, file=saida)
