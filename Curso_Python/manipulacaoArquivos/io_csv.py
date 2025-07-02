import csv

with open('pessoas.csv') as entrada:
    for pessoas in csv.reader(entrada):
        print('Nome {}, Idade {}'.format(*pessoa))

#Essa é forma mais pratica, rapida e segura de fazer o que foi feito nos outros aqruivos
