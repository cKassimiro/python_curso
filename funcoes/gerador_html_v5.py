#!/usr/bin/python3
bloco_atributos = ('accesskey',)
li_atributos = ('type',)


def filtro_atrbts(kwargs, filtro):
    return ' '.join(f'{k}="{v}"' for k, v in kwargs.items() if k in filtro)


def tag_bloco(conteudo, *args, classe='success', inline=False, **kwargs):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args, **kwargs)
    atributos = {'class': classe}
    atributos.update(kwargs)
    return f'{tag}\n {filtro_atrbts(atributos, bloco_atributos + ("class",))}>{html} \n </{tag}'


def tag_lista(*itens, **kwargs):
    lista = ''.join(
        f'<li>{filtro_atrbts(kwargs, li_atributos)}>{item}</li>' for item in itens)
    return f'<ul>{lista}</ul>'


if __name__ == "__main__":
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', classe='info', inline=True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco('falhou', inline=True, classe='error'))
    print(tag_bloco(tag_lista('item 1', 'item 2'), classe='info'))
    print(tag_bloco(tag_lista, 'sabado', 'domingo',
                    classe='info', inline=True))
    print(tag_bloco(tag_lista, 'Sábado', 'Domingo', classe='info',
                    accesskey='m', type='square'))
