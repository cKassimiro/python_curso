class Carro:
    def __init__(self, valor_max,):
        self.valor_max = valor_max
        # self.acelerar = acelerar
        # self.frear = frear

    def acelerar(self, delta):
        print('acelerar', delta)

    def frear(self, delta):
        print('frear', delta)


if __name__ == "__main__":
    c1 = Carro(180, )

    for _ in range(25):
        print(c1.acelerar(8))

    for _ in range(10):
        print(c1.frear(delta=20))
