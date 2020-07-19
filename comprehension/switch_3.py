def get_tipo_dia(dia):
    dias = {
        (1, 7): 'Fim de semana',
        tuple(range(2, 7)): 'Dia de semana'
    }
    dia_escolhido = (tipo for numeros, tipo in dias.items() if dia in numeros)
    return next(dia_escolhido, '** dia invalido **')


if __name__ == "__main__":
    for dia in range(0, 9):
        print(f'{dia}: {get_tipo_dia(dia)}')
