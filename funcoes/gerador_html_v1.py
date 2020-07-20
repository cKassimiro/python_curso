#!/usr/bin/python3
def tag_bloco(texto, classe='success'):
    return f'<div class="{classe}">{texto}</div>'


if __name__ == "__main__":
    print(tag_bloco('bloco'))
