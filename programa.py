print('-='*26)
print('{:^52}'.format(' RESUMO DO PROGRAMA - PROGRAMA PRINCIPAL '))


import pacotes.moeda
preco = float(input('Digite o preço R$ '))
pacotes.moeda.resumo(preco, 20, 12)