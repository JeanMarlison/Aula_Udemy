#!/usr/local/bin/python3
try:
    arquivo = open('pessoas.csv')

    for resgisro in arquivo:
        print('Nome: {} Idade: {}'.format(*resgisro.strip.split(',')))

finally
    print("finally")
    arquivo.close()

# try é um trecho de código que pode ser a riscado!
# finally é uma passagem obrigatória, mesmo que o prgrma dé erro, ele via passar em Finally