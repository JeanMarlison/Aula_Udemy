#!/usr/locar/bin/python3

#Função com * 

def soma2(a,b):
    a + b
    return a + b

def soma3(a, b, c):
    return a + b + c

def somaN(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma


if __name__=='__main__':
    print(soma2(2, 3))
    print(soma3(2, 4, 6))
    print(somaN(1, 2, 3, 4, 5, 6))

#Packing 
#Unpacking