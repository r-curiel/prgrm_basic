"""
Enunciado: Faça a leitura de três valores e apresente como resultado a soma dos quadrados
 dos três valores lidos.

Resolução: 
"""

vector= list()

for n in range(3):

   num = int(input('Insert a number ({0}/3): '.format(n + 1)))

   vector.append(num ** 2)

print(sum(vector))

"""
Comentário: Utilização de uma lista para armazenar as três entradas de dados. Haveria 
possibilidade para operar com list comprehension, porém a construção neste formado pode 
tornar confusa a leitura do código.
"""