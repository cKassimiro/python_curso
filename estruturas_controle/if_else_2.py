#!/usr/bin/python3

def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'Menor de idade'
    elif idade in range(18, 64):
        return 'Adulto'
    elif idade in range(65, 100):
        return 'Melhor idade'
    elif idade >= 100:
        return 'Centenario'
    else:
        return 'Idade Invalida.'

    if __name__ == '__main__':
        for idade in (17, 0, 35, 87, 113, -2):
            # print("""idade {} \n faixa etaria {}"""
            #      .format(idade, faixa_etaria(idade))
            #     )
            print(f'{idade}: {faixa_etaria(idade)}')
