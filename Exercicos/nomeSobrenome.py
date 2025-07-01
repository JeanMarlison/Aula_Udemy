# Exercícios Parte 1
# Dada as listas a seguir:

# primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
# sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
# idades = [19, 28, 25, 31]

# Faça um programa que imprima o dados na seguinte estrutura: "índice - primeiroNome sobreNome está com idade anos".

# Exemplo:
# 0 - João Soares está com 19 anos
#Você deve Utilizar a função enumerate().

# primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
# sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
# idades = [19, 28, 25, 31]

# a = len(primeirosNomes)

# for i in range(a):
#     posicao = i
#     print(f'{primeirosNomes[posicao]} {sobreNomes[posicao]} está com {idades[posicao]} anos')



primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]


for indice, nome in enumerate(primeirosNomes):
    sobrenome = sobreNomes[indice]
    idade = idades[indice]
    print(f"{indice} - {nome} {sobrenome} está com {idade} anos")