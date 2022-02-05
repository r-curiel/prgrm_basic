"""
Enunciado: Leia quatro notas, calcule a média aritmética e imprima o resultado.

Resolução: 
"""

vector1 = list()

for n in range(4):

   num = int(input('Insert the {0}/4 grade: '.format(n + 1)))

   vector1.append(num)

average = sum(vector1) / 4

print(average)

"""
Comentário: A resolução poderia agrupar funções através da list comprehension, 
entretanto, para fluidez da leitura do código, optei por deixar extenso mas com etapas 
bem definidas.
"""