#!/usr/bin/python3

for i in range(1, 11):
    print('i = {}'.format(i))

for j in range(10):
    print('i = {}'.format(i))

for x in range(1, 11):
    for y in range(1, 11):
        print("{} * {} = {}".format(x, y, x * y))
        # print(f'{x} * {y} = {x * y}')
