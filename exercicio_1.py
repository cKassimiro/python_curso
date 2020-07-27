# RECEBER PREÇO E CATEGORIA
def calc_imp(cond, categ, produto):
    if cond == 'S' or categ == 2:
        return produto*0.05
    else:
        return produto*0.08


def preco(produto, categ):
    print(produto)
    for i in range(0, 26):
        if produto == i:
            for j in range(1, 4):
                j == categ
                if categ == 1:
                    return produto + produto*0.05
                elif categ == 2:
                    return produto + produto*0.08
                elif categ == 3:
                    return produto + produto*0.10
    if produto > 25:
        if categ == 1:
            return produto + produto*0.12
        elif categ == 2:
            return produto + produto*0.15
        elif categ == 3:
            return produto + produto*0.18


valor = float(input('Insira o valor: '))
print(7*'*' + 'TIPO' + 7*'*')
print('1 - Limpeza\n'
      '2 - Alimentação\n'
      '3 - Vestuario\n')
tipo = int(input('Insira a categoria: '))
refri = str(
    input('É necessario sistema de refrigeração? S/N '))

valor_imp = calc_imp(cond=refri, categ=tipo, produto=valor)
valor_total = preco(valor, tipo) + valor_imp
print(valor_total)
