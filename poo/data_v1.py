class Data:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def to_str(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


# INSTANCIA
d1 = Data(26, 3, 2001)  # METODO CONSTRUTOR

# ATRIBUTOS
# d1.data = 26
# d1.mes = 3
# d1.ano = 2001

# INSTANCIA
d2 = Data(4, 8, 2020)  # METODO CONSTRUTOR

# ATRIBUTOS
# d2.data = 4
# d2.mes = 8
# d2.ano = 2020

print(d1.to_str())
# OU
print(d2.to_str())
