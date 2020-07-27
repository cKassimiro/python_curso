def calc_horas(hora, falta):
    return hora_extra - 2/3*(hora_extra - hora_falta)


def consulta(media):
    if media > 2400:
        return print('Premio: R$ 1500')
    elif media > 1800 and media < 2399:
        return print('Premio: R$ 1000')
    elif media > 1200 and media < 1799:
        return print('Premio: R$ 890')
    elif media < 1200:
        return print('Premio: R$ 500')


hora_extra = float(input('Horas extras prestadas: '))
hora_falta = float(input('Horas faltadas: '))

h = calc_horas(hora=hora_extra, falta=hora_falta)
consulta(media=h)
