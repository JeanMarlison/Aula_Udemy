# A função map ela tem como objetivo de mapear um objeto em outro
lista1 = [1, 2, 3]
dobro = map(lambda x: x * 2, lista1)
print(list(dobro))

lista2 = [
    {'nome': 'João', 'idade': 31},
    {'nome': 'Maria', 'idade': 37},
    {'nome': 'José', 'idade': 26}
]

soNomes = map(lambda p: p['nome'], lista2)
print(list(soNomes))

soIdades = map(lambda p: p['idade'], lista2)
print(sum(soIdades))


