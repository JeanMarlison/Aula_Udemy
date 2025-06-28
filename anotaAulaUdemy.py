# %% O comando '%%' em IDEs como VS Code ou Spyder cria uma célula executável.
# Não é um comando padrão do Python, mas é útil para testes rápidos.
print("Célula de código para testes rápidos.")


# --- INTERPOLAÇÃO DE STRINGS ---
nome, idade = 'Jean', 24

# Método 1: Estilo antigo com % (ainda funcional)
print('Nome: %s Idade: %d' % (nome, idade))

# Método 2: .format() (versátil, disponível desde o Python 2.6)
print('Nome: {0} Idade: {1}'.format(nome, idade))

# Método 3: f-string (moderno e recomendado, a partir do Python 3.6)
print(f'Nome: {nome} Idade: {idade}')



# --- ESTRUTURA DE CONTROLE ---

# Função para auxiliar.

def obterConceitoNota(valor):
    nota = float(valor)

    if nota > 10 or nota < 0:
        return "Nota inválida (deve ser entre 0 e 10)"
    elif nota >= 9.0:
        return "E (Excelente)"
    elif nota >= 7.0:
        return "B (Bom)"
    elif nota >= 5.0:
        return "R (Regular)"
    else: # Se a nota for menor que 5.0
        return "I (Insuficiente)"

# Ele deve estar no nível principal do script (sem recuo).
if __name__ == "__main__":
    valor_informado = input('Digite a nota do aluno: ')
    conceito = obterConceitoNota(valor_informado)
    print(conceito)