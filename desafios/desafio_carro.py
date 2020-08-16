class Carro:
    def __init__(self, valor_max, valor_atual=0):
        self.valor_max = valor_max
        self.valor_atual = valor_atual

    def acelerar(self, delta):
        self.valor_atual = self.valor_atual + delta
        if self.valor_atual > self.valor_max:
            self.valor_atual = self.valor_max
        return print('acelerar', self.valor_atual)

    def frear(self, delta):
        self.valor_atual = self.valor_atual - delta
        if self.valor_atual < 0:
            self.valor_atual = 0
        return print('frear', self.valor_atual)


if __name__ == "__main__":

    c1 = Carro(180)

    for _ in range(25):
        print(c1.acelerar(delta=8))

    for _ in range(10):
        print(c1.frear(delta=20))
