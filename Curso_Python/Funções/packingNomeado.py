#Kwargs
def resultadosF1(primeiro, segundo, terceiro):
    print(f'1) {primeiro}')
    print(f'2) {segundo}')
    print(f'3) {terceiro}')


if __name__=='__main__':
    podium = {'segundo': 'Fulano',
              'primeiro':'Jean',
              'terceiro':'bertano'}
resultadosF1(**podium)

# Neste caso é um exemplo de Unpecking, onde estamos passando um dicionario em pacotado para uma função