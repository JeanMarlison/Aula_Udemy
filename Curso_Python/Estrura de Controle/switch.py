#Não tem nativamente SWITCH em python, vamos simular com função e diconario
def getDiaSemana(dia):
    dias = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta', 
        6: 'Sexta',
        7: 'Sábado',
    }
    return dia.get(dia, '** Inválido **')

    if __name__ == '__main__':
        for dia in range(0, 9):
            print(f'{dia}: {getDiaSemana}')


