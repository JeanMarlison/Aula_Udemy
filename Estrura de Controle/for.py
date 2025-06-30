# Esse FOR vai de 1 até 10
for i in range(1, 11):
    print('i = {}'.format(i))

for j in range(1, 11):
    print('J = {}'.format(j))


for x in range(1, 11):
    for y in range(1, 11):
        print(f'{X} * {y} = {x * y}')


# -------------- Para percorrer: 
palavra = 'Paralelepítido'
for letra in palavra:
    print(letra)

for testeLetra in palavra:
    print(testeLetra, end=",") # Para exibir na mesma linha
print("Fim")

testeLista = ['Jean', 'Fulano', 'Ciclano', 'Bertano']
for nome in testeLista:
    print(nome)


for posicao, nome in enumerate(testeLista):
    print(f'{posicao + 1})', nome)

diasSemana = ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado')

for dia in diasSemana:
    print(f'Hoje é {dia}')

for letra in set('Muito legal'):
    print(letra)

#For para percorrer dicioanrio 

produto = {'nome': 'Caneta Chic', 'preco': 14.99,
            'importada':True, 'estoque': 793}

#Comun por chaves
for chave in produto:
    print(chave)

#Por valor
for valor in produto.values():
    print(valor)

#Chave e Valor
for chave, valor in produto.intems():
    print(chave, '=' valor)


# As vareveis estão disponveis despos que foram usadas no for
print(chave, valor)