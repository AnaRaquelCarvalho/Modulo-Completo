print('-='*26)
print('{:^52}'.format(' RESUMO DO PROGRAMA - PROGRAMA PRINCIPAL '))


import modulos.Funçoes
import modulos.dados
preco = modulos.dados.leiaDinheiro('Digite o preço R$ ')
modulos.Funçoes.resumo(preco, 20, 12)