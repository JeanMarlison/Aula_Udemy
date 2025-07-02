#!/usr/local/bin/python3
arquivo = open('pessoas.csv')
for resgisro in arquivo:
    print('Nome: {} Idade: {}'.format(*resgisro.split(',')))
arquivo.close()