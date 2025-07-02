compras = (
    {'quntidade': 2, 'preco':10},
    {'quntidade': 3, 'preco':20},
    {'quntidade': 5, 'preco':14},

)

def calPrecoTotal(compra):
    return compra['quntidade'] * compra['preco']

# pode ficar desa forma a Fucao: 
# def calPrecoTotal(compra): return compra['quntidade'] * compra['preco']

totias = tuple(map(calPrecoTotal, compras))



print('Preços totais:', list(totias))
print('Total geral:', sum(totias))