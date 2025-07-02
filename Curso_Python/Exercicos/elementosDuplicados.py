# Exercícios Parte 1
# Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Utilize a lista a seguir para testar sua função.

# ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

# listaFornecida = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
# novaLista = []


# for i in listaFornecida:
#     if i not in novaLista:
#         novaLista.append(i)
        
        
# print(novaLista)

listaFornecida = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

novaLista = list(set(listaFornecida))
print(novaLista)

