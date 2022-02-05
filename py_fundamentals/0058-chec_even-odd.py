"""
Enunciado: Escreva um programa que, dados dois números inteiros, mostre na tela o 
maior deles, assim como a diferença existente entre ambos.

Resolução: 
"""

nbrs = [int(input(f"Insert the {n+1}/2 number: ")) for n in range(2)]

print(f'The maximum number is: {max(nbrs)}')

if min(nbrs) < 0:
   print(f'The difference between {max(nbrs)} and {min(nbrs)} is {max(nbrs) + abs(min(nbrs))}')
else:
   print(f'The difference between {max(nbrs)} and {min(nbrs)} is {max(nbrs) - min(nbrs)}')


"""
Comentário: A resolução do código consistiu na coleta das informações e retorno do 
resultado das operações. O código ficou extenso em função da necessidade de tratamento 
da entrada de valores negativos, trabalhados no 'if'.
"""