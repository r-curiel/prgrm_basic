"""
Enunciado: Receba um número inteiro entre 1 e 7 e imprima o dia da semana correspondente 
a este numero. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.

Resolução: 
"""

semana = ['Domingo', 'Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sábado']


dia_semana = {v + 1: k for v, k in enumerate(semana)}


while True:
   try:
       valor = input('Dia da semana: ')
       if 0 < int(valor) < 8:
           print(f"O dia da semana para {valor} é {dia_semana.get(int(valor))}.")
       else:
           print('### Entrada inválida - Operação encerrada ###')
           break
   except:
       print('### Entrada inválida - Operação encerrada ###')
       break


"""
Comentário: A resolução do código gerou chaves de 1 a 7 correspondente a cada dia da 
semana. A análise do valor levou em consideração o tipo de dado de entrada (requerido 
número inteiro no intervalo de chaves), cuja inadequação apresenta uma mensagem de erro 
que leva ao encerramento do programa.
"""