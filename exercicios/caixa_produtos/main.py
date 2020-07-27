from funcoes import taxas

valor = float(input('Insira o valor: '))
print(7*'*' + 'TIPO' + 7*'*')
print('1 - Limpeza\n'
      '2 - Alimentação\n'
      '3 - Vestuario\n')
tipo = int(input('Insira a categoria: '))
refri = str(
    input('É necessario sistema de refrigeração? S/N '))

valor_imp = taxas.calc_imp(cond=refri, categ=tipo, produto=valor)
valor_total = taxas.preco(valor, tipo) + valor_imp
print(f'R$ {valor_total}')
