```markdown
# 🚀 Projeto de Análise de Dados com Python

Este projeto explora a análise de dados utilizando as principais bibliotecas do ecossistema Python. A base de dados foi obtida do [Kaggle](https://www.kaggle.com/), uma excelente plataforma para encontrar datasets e praticar suas habilidades em ciência de dados.

## 🐼 Pandas: O Canivete Suíço da Análise de Dados

**Pandas** é a biblioteca fundamental para manipulação e análise de dados em Python. Ela nos permite trabalhar com dados tabulares (como planilhas do Excel ou tabelas de um banco de dados) de forma intuitiva e poderosa.

Com o Pandas, podemos ir muito além do que o Python puro oferece para análise de dados. Ele é a ferramenta ideal para:

*   📖 **Ler e Escrever Dados:** Carregar informações de arquivos como `.csv`, `.xlsx`, e muitos outros.
*   🔎 **Explorar e Filtrar:** Selecionar linhas e colunas específicas para focar no que é importante.
*   🧹 **Limpar e Transformar:** Modificar dados, tratar valores ausentes e preparar as informações para análise.
*   📊 **Analisar e Agregar:** Responder perguntas de negócio como:
    *   *Qual o produto mais vendido?*
    *   *Qual vendedor teve o maior faturamento?*
    *   *Qual a média de preço por categoria?*
*   📈 **Visualizar:** Integrar-se facilmente com bibliotecas como Matplotlib e Seaborn para criar gráficos incríveis.

### O DataFrame

A principal estrutura do Pandas é o **`DataFrame`**, uma tabela bidimensional onde:
*   **Linhas (`rows`):** Representam uma observação ou registro individual.
*   **Colunas (`columns`):** Representam uma variável ou característica.

> [Acesse a Documentação Oficial do Pandas](https://pandas.pydata.org/docs/)

---

## ⚡ NumPy: O Motor de Alta Performance

**NumPy** (Numerical Python) é a biblioteca que serve como alicerce para a computação científica em Python. Enquanto o Pandas organiza os dados, o NumPy fornece o poder de processamento numérico por baixo dos panos.

Seu principal superpoder é fornecer um objeto de array multidimensional que é **extremamente rápido e eficiente em memória** para manipular grandes volumes de números.

### Arrays Multidimensionais

NumPy trabalha com `arrays`, que podem ter diferentes dimensões. Podemos verificar a "forma" (dimensões) de um array com o atributo `.shape`:

*   **Array 1D (Vetor):** Uma única lista de números.
    *   Exemplo: `[1, 5, 10, 25]`
    *   `.shape` será `(4,)`

*   **Array 2D (Matriz):** Uma tabela com linhas e colunas, como uma planilha.
    *   Exemplo: `[[1, 2, 3], [4, 5, 6]]`
    *   `.shape` será `(2, 3)` (2 linhas, 3 colunas)

*   **Array 3D (Cubo):** Um conjunto de tabelas. Pense em uma imagem colorida (altura, largura, canais de cor RGB).
    *   `.shape` poderia ser `(3, 10, 10)` (3 matrizes de 10x10)

> [Acesse a Documentação Oficial do NumPy](https://numpy.org/)

---

## 📈 Matplotlib: A Tela e os Pincéis para seus Dados

Se "uma imagem vale mais que mil palavras", **Matplotlib** é a biblioteca que nos permite "pintar" a história que nossos dados contam. É a ferramenta mais tradicional e poderosa para criar visualizações estáticas, animadas e interativas em Python.

Enquanto Pandas e NumPy nos ajudam a preparar e analisar os números, Matplotlib os transforma em insights visuais claros e compreensíveis.

### O que podemos criar?

Com Matplotlib, você tem controle total para construir uma vasta gama de gráficos, como:

*   📊 **Gráficos de Linha:** Para ver tendências ao longo do tempo.
*   📊 **Gráficos de Barra:** Para comparar categorias.
*   📊 **Histogramas:** Para entender a distribuição dos seus dados.
*   📊 **Gráficos de Dispersão (Scatter Plots):** Para visualizar a relação entre duas variáveis.
*   📊 **Gráficos de Pizza:** Para mostrar a proporção de cada parte em um todo.
*   ...e muito mais!

### A Anatomia de um Gráfico

Para começar, é útil entender duas partes principais de um gráfico Matplotlib:

*   **`Figure` (Figura):** Pense nela como a tela em branco, a janela inteira onde tudo será desenhado.
*   **`Axes` (Eixos):** É a área de plotagem em si, onde os dados são desenhados com seus eixos (x, y), títulos e legendas. Uma única `Figure` pode conter vários `Axes`.

Aqui está um exemplo básico de como criar um gráfico simples:

```python
import matplotlib.pyplot as plt
import numpy as np

# 1. Preparando os dados
x = np.linspace(0, 10, 100) # Cria 100 números de 0 a 10
y = np.sin(x)              # Calcula o seno de cada número

# 2. Criando a Figure e os Axes
fig, ax = plt.subplots()

# 3. Plotando os dados nos Axes
ax.plot(x, y)

# 4. Customizando o gráfico
ax.set_title("Gráfico de uma Função Seno")
ax.set_xlabel("Eixo X")
ax.set_ylabel("Eixo Y")

# 5. Exibindo o gráfico
plt.show()