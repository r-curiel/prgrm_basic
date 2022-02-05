"""
Enunciado: Peça ao usuário para digitar três valores inteiros e imprima a soma deles.

Resolução (convencional): 


lista = list()

for n in range(3):

   number = int(input(f"Insert the {n+1}/3 number: "))

   lista.append(number)

print(f"The sum of the values is: {sum(lista)}")



Resolução (alternativa): 
"""

print(f"The sum of values is: {sum([int(input(f'Insert the {n + 1}/3 number: ')) for n in range(3)])}")



"""
Comentário: A resolução convencional utiliza um loop for para incrementar três 
entradas em uma lista, imprimindo a soma dos valores no final. A resolução alternativa 
utiliza list comprehension para otimizar as entradas ao mesmo tempo que cria uma lista 
e a alimenta. A vantagem da resolução alternativa é a otimização da quantidade de linhas 
de código, mas sua desvantagem é que pode gerar confusão.
"""