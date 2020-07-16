#!/usr/bin/python3

for x in range(1, 11):
    if x % 2 == 0:  # verifica numeros impares
        continue
    print(x)

for x in range(1, 11):
    if x == 5:
        break
    print(x)
    print("tavs")
