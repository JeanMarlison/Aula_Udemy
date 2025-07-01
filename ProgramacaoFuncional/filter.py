# A função filter sempre vai retorna um verdadeiro ou falso se for verdade ele inclui na lista!

pessoas = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17}
]


menores = filter(lambda p: p['idades' < 18, pessoas])
print(list(menores))