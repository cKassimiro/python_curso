PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')
textos = [
    "João gosta muito de futebol\n",
    "Felipe gosta de ir a praia\n",
    "Jonas estuda religião\n",
    "Fabio pretente entrar na política\n",
    "Joana tem uma boneca\n",
]

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print("Textos proibidos por conta da(s) palavra(s):", palavra)
            break

    else:
        print("Textos autorizados:", texto)
