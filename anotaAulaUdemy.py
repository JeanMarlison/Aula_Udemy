
print(" #%% Esse comando serve para execultar códigos de forma rapida")


# INTEROLAÇÂO

nome, idade = 'Jean', 24

print('Nome: %s Idade: %d' % (nome, idade))
print('Nome: {0} Idade: {1}'.format(nome, idade)) # Versão Python > 3.6
print(f'Nome {nome} Idade: {idade}') # Versão Python >= 3.6

# --- Estrura de Controle

#Vam ciar uma Função para auxliar. 
def nota_conceito(valor):
    nota = float(valor)
# ---
    if nota > 10:
        return "Nota inválida"
    elif nota >= 9.1 or nota == 10:
        return "(E - EXC) Excelente"
    elif nota >= 7.0 or nota == 8.9:
        return "(B - BOM) Bom"
    elif nota >= 5.0 or nota == 6.9:
        return "(R - REG) Regular"
    else:
        return "(I - INS) Insuficiente "
    
    # Para poder chamar a função tamos que está dentro do modo
    # Principal MAIN: if__name__ == '__main__':

    if __name__ == "__main__":
        valor_informado = input('Nota do Aluno')
        conceito = nota_conceito(valor_informado)
        print(conceito)