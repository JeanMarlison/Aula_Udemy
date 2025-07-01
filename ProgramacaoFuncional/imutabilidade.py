from functools import reduce
from operator import add

valores = [30, 10, 25, 70, 100, 94]


# Aqui não altera o valores
print(sorted(valores))
print(valores)


# Aqui altera a vareaval valores
# valores.sort()
# print(valores)

print(min(valores))
print(max(valores))

print(sum(valores))
print(reduce(add, valores))

print(valores) 
# Nada foi alterado, poies estamos usando a imutabilidade meto(aquiDentroOResto)
# Diferente de OResto.metodo(), aqui vai mudar

print(reversed(valores))
print(valores)

# valores.reverse()
# print(valores)
# -----
# Dê preferência para dados imutaveis metodo(aquiFunçãoOuVareavel), pois isso faz com que o seu program fique mais "previsivel".

