PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}
textos = [
    "João gosta muito de futebol\n",
    "Felipe gosta de ir a praia\n",
    "Jonas estuda religião\n",
    "Fabio pretente entrar na política\n",
    "Joana tem uma boneca\n",
]

for texto in textos:
    intersec = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersec:
        print('Texto possui palavras proibidas', intersec)

    else:
        print('Texto autorizado:', texto)
