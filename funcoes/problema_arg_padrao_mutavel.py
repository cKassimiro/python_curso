#!/usr/bin/python3

def fibonacci(sequencia=[0, 1]):
    # Uso de mutaveis como valor default (armadilha)
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == "__main__":
    inicio = fibonacci()
    print(inicio, id(inicio))
    print(fibonacci(inicio))
    restart = fibonacci()
    print(restart, id(restart))

# A *LISTA* "SEQUENCIA", POR SER *MUTAVEL*, AO LONGO DO PROCESSO
# É ALTERADA MUDANDO O VALOR DEFAULT (PADRAO) QUE DEVERIA SER
# ESTATICO

# UMA DAS POSSIVEIS SOLUÇÕES: USAR *TUPLA()* NO LUGAR DE *LISTA[]*
