#-----------------------------------------------------
# Laço de Repetição
#Enquanto for verdade ele vai fazer!
from random import randint

numeroInformado = -1
numeroSecreto = randint(0, 9)

while numeroInformado != numeroSecreto:
    numeroInformado = int(input('Informe o número: '))

print('Número secreto {} foi encontrado!'.format(numeroSecreto))
