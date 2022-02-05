"""
Enunciado: Receba um número inteiro entre 1 e 12 e imprima o mês correspondente a este 
numero. Isto é, janeiro se 1, fevereiro se 2, e assim por diante.

Resolução: 
"""

mes = ['Janeiro', 'Fevereiro', 'Março','Abril',
      'Maio','Junho', 'Julho', 'Agosto',
      'Setembro', 'Outubro', 'Novembro', 'Dezembro']

mes = {v + 1: k for v, k in enumerate(mes)}

while True:
  try:
      valor = input('Mês do ano: ')
      if 0 < int(valor) < 8:
          print(f"O mês {valor} é {mes.get(int(valor))}.")
      else:
          print('### Entrada inválida - Operação encerrada ###')
          break
  except:
      print('### Entrada inválida - Operação encerrada ###')
      break


"""
Comentário: A resolução do código seguiu o padrão da resolução anterior.
"""