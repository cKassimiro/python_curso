def get_dia(dia):
    dias = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Ternça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sabado',
    }
    return dias.get(dia, '** invalido **')


if __name__ == '__main__':
    for dia in range(1, 8):
        if dia == 1 or dia == 7:
            print('{}, {}, fim de semana'.format(dia, get_dia(dia)))
            continue
        print('{}, {} dia de semana'.format(dia, get_dia(dia)))
