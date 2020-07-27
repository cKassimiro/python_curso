def calc_imp(cond, categ, produto):
    if cond == 'S' or categ == 2:
        return produto*0.05
    else:
        return produto*0.08


def preco(produto, categ):
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
