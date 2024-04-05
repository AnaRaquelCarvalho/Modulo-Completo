print('{:^52}'.format(' E SUAS FUNÇÕES '))
print('-='*26)

def aumentar(preço = 0, taxa = 0, format = False):
    resultado = preço + (preço * taxa/100)
    return resultado if format is False else moeda(resultado)

def diminuir(preço = 0, taxa = 0, format = False):
    resultado = preço - (preço * taxa/100)
    return resultado if format is False else moeda(resultado)

def metade(preço = 0, format = False):
    resultado = preço / 2
    return resultado if not format is False else moeda(resultado)

def dobro(preço = 0, format = False):
    resultado = preço * 2
    return resultado if not format is False else moeda(resultado)

def moeda(preço = 0, moeda = 'R$ '):
    return f'{moeda}{preço:.2f}'.replace('.',',')

def resumo(preço = 0, taxa=10, taxar = 5):
    print('-='*26)
    print('RESUMO DO VALOR'.center(30))
    print()
    print(f'Preço Analisado: {moeda(preço)}')
    print(f'Metade do preço: {metade(preço, True)}')
    print(f'O dobro do preço:{dobro(preço, True)}')
    print(f'Com aumento {taxa} %, o valor fica {aumentar(preço, taxa, True)}')
    print(f'Com a Diminuição {taxar}%, o valor fica {diminuir(preço, taxar, True)}')
    print('-='*26)