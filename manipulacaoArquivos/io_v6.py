#!/usr/local/bin/python3

# Com o primeiro With vamos abrir o Arquivo, com o segundo vamos Escrever 
# OBS: Nesta escrita, não vamos escrever no Aquivo, vai ser criado um novo! 
# No segundo WITH (Primero lado é o nome do Aqruivo , Segundo é modo que neste caso é o 'w' mode de escrita)
# pessoas.txt vai ser o aquivo de saida, ou seja as altereções vão para o mode de saida que é o txt


with open('pessoas.csv') as arquivo: 
    with open('pessoas.txt', 'w') as saida:
        for resgisro in arquivo:
            pessoa = resgisro.strip().split(',')
            print('Nome: {} Idade: {}'.format(*pessoa), file = saida) 
            # Esse pint em vez de ser no console via ser direto dentro Arquivo TXT
            # Podemos monipular onde via ser imprimido as coisas

if arquivo.close:
    print('Arquivo foi fechado!')
