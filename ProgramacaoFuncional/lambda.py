compras = (
    {'quntidade': 2, 'preco':10},
    {'quntidade': 3, 'preco':20},
    {'quntidade': 5, 'preco':14},

)
totias = tuple(map(lambda compra: compra['quntidade']* compra['preco'], compras))

print('Preços totais:', list(totias))
print('Total geral:', sum(totias))