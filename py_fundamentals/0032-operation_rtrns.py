"""
Enunciado: Leia um número inteiro e imprima a soma do sucessor de seu triplo com o 
antecessor de seu dobro.

Resolução: 
"""

num = int(input('Insert a number: '))

print((((num * 3) + 1) + ((num * 2) - 1)))

"""
Comentário: A resolução do código exigiu aproveitamento do exercício 31, incluindo 
hierarquia de operações para tender ao que foi exigido no enunciado.
"""