#!/usr/local/bin/python3

with open('pessoas.csv') as arquivo

    for resgisro in arquivo:
        print('Nome: {} Idade: {}'.format(*resgisro.strip.split(',')))

if arquivo.close:
    print('Arquivo foi fechado!')


# With, ele fecha o arquivo. Ele fecha tudo que foi execuldado dentro do Bloco de Código quando chergar no fim da execusão!
# É a melhor escolha quando vai se trabalhor com recursos que no final tenham que ser fechados.