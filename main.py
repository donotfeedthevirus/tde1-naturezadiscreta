'''
Nome do Aluno: Gustavo Muniz Scheiffer

Enunciado:Para obter os pontos relativos a este trabalho, você deverá criar um programa, utilizando a
linguagem Python, C, ou C++. Este programa, quando executado, irá apresentar os resultados de
operações que serão realizadas entre dois conjuntos de dados.
O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt)
contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas
em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas
segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de
operações que estão descritas no arquivo, este número de operações será um inteiro; as linhas
seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código da
operação (U para união, I para interseção, D para diferença e C produto cartesiano), a segunda e
terceira linhas conterão os elementos dos conjuntos separados por virgulas. A seguir está um exemplo
das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver:
4
U
3, 5, 67, 7
1, 2, 3, 4
I
1, 2, 3, 4, 5
4, 5
D
1, A, C, 34
A, C, D, 23
C
3, 4, 5, 5, A, B, R
1, B, C, D, 1
Neste exemplo temos 4 operações uma união (U), uma interseção (I), um diferença (D) e um
produto cartesiano (C). A união, definida por U, deverá ser executada sobre os conjuntos {𝟑, 𝟓, 𝟔𝟕, 𝟕} e
{𝟏, 𝟐, 𝟑, 𝟒}, cujos elementos estão explicitados nas linhas posteriores a definição da operção (U).
A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados
dos conjuntos identificados, e o resultado da operação. No caso da união a linha de saída deverá conter
a informação e a formatação mostrada a seguir:
União: conjunto 1 {3, 5, 67, 7}, conjunto 2 {1, 2, 3, 4}. Resultado: {3, 5, 67, 7, 1, 2, 4}
Seu programa deverá mostrar a saída no terminal, ou em um arquivo de textos. Em qualquer
um dos casos, a saída será composta por uma linha de saída para cada operação constante no arquivo
de textos de entrada formatada segundo o exemplo de saída acima. Observe as letras maiúsculas e
minúsculas, e os pontos utilizados na formatação da linha de saída apresenta acima.
No caso do texto de exemplo, teremos 4 linhas, e apenas 4 linhas de saída, formatadas e
pontuadas conforme o exemplo de saída acima. O uso de linhas extras na saída, ou erros de formatação,
implicam em perda de pontos como pode ser visto na rubrica de avaliação constante neste documento.
'''

def ler_arquivo_entrada(caminho_arquivo):
  with open(caminho_arquivo, 'r') as arquivo:
      num_operacoes = int(arquivo.readline().strip())
      operacoes = []
      for _ in range(num_operacoes):
          codigo_operacao = arquivo.readline().strip()
          conjunto1 = arquivo.readline().strip().split(', ')
          conjunto2 = arquivo.readline().strip().split(', ')
          operacoes.append((codigo_operacao, conjunto1, conjunto2))
  return operacoes

def uniao(conjunto1, conjunto2):
  return conjunto1 + [item for item in conjunto2 if item not in conjunto1]

def intersecao(conjunto1, conjunto2):
  return [item for item in conjunto1 if item in conjunto2]

def diferenca(conjunto1, conjunto2):
  return [item for item in conjunto1 if item not in conjunto2]

def produto_cartesiano(conjunto1, conjunto2):
  return [(x, y) for x in conjunto1 for y in conjunto2]

def formatar_conjunto(conjunto):
  return "{" + ", ".join(conjunto) + "}"

def processar_operacoes(operacoes):
  resultados = []
  for operacao in operacoes:
      codigo, conjunto1, conjunto2 = operacao

      if codigo == 'U':
          resultado = uniao(conjunto1, conjunto2)
          descricao = f"União: conjunto 1 {formatar_conjunto(conjunto1)}, conjunto 2 {formatar_conjunto(conjunto2)}. Resultado: {formatar_conjunto(resultado)}"

      elif codigo == 'I':
          resultado = intersecao(conjunto1, conjunto2)
          descricao = f"Interseção: conjunto 1 {formatar_conjunto(conjunto1)}, conjunto 2 {formatar_conjunto(conjunto2)}. Resultado: {formatar_conjunto(resultado)}"

      elif codigo == 'D':
          resultado = diferenca(conjunto1, conjunto2)
          descricao = f"Diferença: conjunto 1 {formatar_conjunto(conjunto1)}, conjunto 2 {formatar_conjunto(conjunto2)}. Resultado: {formatar_conjunto(resultado)}"

      elif codigo == 'C':
          resultado = produto_cartesiano(conjunto1, conjunto2)
          descricao = f"Produto Cartesiano: conjunto 1 {formatar_conjunto(conjunto1)}, conjunto 2 {formatar_conjunto(conjunto2)}. Resultado: {resultado}"

      resultados.append(descricao)

  return resultados

def salvar_resultado(resultados, caminho_saida):
  with open(caminho_saida, 'w') as arquivo_saida:
      for resultado in resultados:
          arquivo_saida.write(resultado + "\n")

#Altere o número do arquivo de entrada para o arquivo de entrada desejado (entrada1, entrada2, etc.)
caminho_entrada = 'entrada1.txt'
caminho_saida = 'saida.txt'

operacoes = ler_arquivo_entrada(caminho_entrada)

resultados = processar_operacoes(operacoes)

salvar_resultado(resultados, caminho_saida)

for resultado in resultados:
  print(resultado)
