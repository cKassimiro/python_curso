import re
from typing import List, Dict

pessoas: List[Dict[str, str]] = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Moreira'},
    {'nome': 'Elaine', 'sobrenome': 'Figueiredo'},
    {'nome': 'Helena', 'sobrenome': 'Oliveira'},
    {'nome': 'vivian', 'sobrenome': 'Silva'},
    {'nome': 'Fabrício', 'sobrenome': 'Costa'},
    {'nome': 'Eduardo', 'sobrenome': 'Vieira'},
    {'nome': 'Lívia', 'sobrenome': 'Madeira'},
    {'nome': 'João', 'sobrenome': 'Barbosa'},
    {'nome': 'Dania', 'sobrenome': 'Maia'},
]


def busca_pessoa(
    pessoas: List[Dict[str, str]], nome_buscado: str
) -> Dict[str, str]:
    for pessoa in pessoas:
        nome, sobrenome = pessoa.values()

        if nome_buscado == f'{nome} {sobrenome}':
            return pessoa

        regex = re.compile(fr'{nome}\s+{sobrenome}', flags=re.I)
        if regex.search(nome_buscado):
            return pessoa

    return {}


if __name__ == "__main__":
    pessoa_1 = busca_pessoa(pessoas, 'helena  Oliveira')
    pessoa_2 = busca_pessoa(pessoas, 'João barbosa')
    print(pessoa_1)
    print(pessoa_2)
