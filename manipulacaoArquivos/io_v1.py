#!/usr/local/bin/python3

#Aqui é para lever o arquivo
arquivo = open('pessoas.csv')

#Para Receber esses dados do Aquivo
dados = arquivo.read()

#Fechar o Arquivo
arquivo.close() # Para liberer os recursos que estavam sendo usados pelo arquivo.

#Agora vamos percorrer este Arquivo
for registro in dados.splitlines():
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))