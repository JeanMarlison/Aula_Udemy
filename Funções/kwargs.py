def resultadosF1(**podium):
    for posicao, piloto in podium.items():
        print(f'{posicao} -> {piloto}' )

if __name__=='__main__':
    resultadosF1(primeiro='Jean',
                 segundo='Fulano',
                 terceiro='bertano')
    

    # Aqui estamos passando um dissonario para uma função que vai empacotar.