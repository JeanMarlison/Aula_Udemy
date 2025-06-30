#!/usr/local/bin/python3
arquivo = open('pessoas.csv')

for resgisro in arquivo:
    print('Nome: {} Idade: {}'.format(*resgisro.strip.split(',')))

arquivo.close()


#Strip() é usado pare LIMPAR o que você passa dentro de () se não tiver nada ele vai apagar os espaços em braco das bordas.